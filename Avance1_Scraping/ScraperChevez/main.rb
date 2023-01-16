require 'open-uri' #consultar a la plataforma
require 'nokogiri' #formatear, parsear a html
require 'csv' #escribir y leer csv
# require './ArchivoProyecto'

END {
  puts "Scraper de StackOverflow - Kevin Chevez"
  archivo = ArchivoProyecto.new("dataset-kchevez", 20)
  archivo.crearArchivos()
}

BEGIN {
  class ArchivoProyecto
    attr_accessor :filename, :n_pages

    def initialize(filename, n_pages)
      @filename = filename
      @n_pages = n_pages
    end
  
    def crearArchivos
      # Escribimos la cabeceras del archivo
      escribirCabecera
      page = 1
      numero = 1
      while page <= @n_pages
        link = if page == 1
                 'https://stackoverflow.com/jobs/companies'
               else
                 "https://stackoverflow.com/jobs/companies?pg=#{page}"
               end
  
        puts "Scrapeando la url #{link}"
        stackOverflowCompaniesHTML = URI.open(link)
        datos = stackOverflowCompaniesHTML.read
        parsed_content = Nokogiri::HTML(datos)
  
        parsed_content.css('.dismissable-company').each do |contenedor_pregunta|
          # CompaniesStackOverFlow: numero, empresa, habilidades
          arr_habilidades = []
          contenedor_estadistica = contenedor_pregunta.css('.d-flex > div.fl1')
          link_nuevo = contenedor_estadistica.css('h2.fs-body2').css('a').attr('href')
          link_nuevo = 'https://stackoverflow.com' + link_nuevo
          arr_link_splited = link_nuevo.split('?', -1)
          link_nuevo = arr_link_splited[0]
          empresa = contenedor_estadistica.css('h2.fs-body2').inner_text.strip
          contenedor_estadistica.css('div.gs4').css('a.s-tag').each do |etiqueta|
            arr_habilidades.push(etiqueta.inner_text.strip)
          end
  
          #------------------------ REALIZANDO UN NUEVO SCRAPING AL CONTENIDO INTERNO DE LA INFORMACION DE LA EMPRESA. ------------------------
          puts "Scrapeando la el contenido interno de la info de la empresa #{empresa} en el link: #{link_nuevo}\n"
          sOCompaniesHTML = URI.open(link_nuevo)
          datos_inner_info = sOCompaniesHTML.read
          parsed_content_inner_info = Nokogiri::HTML(datos_inner_info)
          
          parsed_content_inner_info.css('div#tech-stack-items').css('div.fw-wrap').css('a.flex--item').each do |etiqueta|
            arr_habilidades.push(etiqueta.inner_text.strip())
            # puts etiqueta.inner_text.strip()
          end
          #------------------------------------------------------------------------------------------------------------------------------------
  
          # puts 'Empresa: ' + empresa
  
          empresaInfoSO = EmpresaInfoStackOverflow.new(numero, empresa, arr_habilidades.join(';'))
          empresaInfoSO.guardarEmpresaInfoSO("#{@filename}.csv")
          numero += 1
        end
        page += 1
        # puts ""
      end
    end
  
    def escribirCabecera
      CSV.open("#{@filename}.csv", 'w') do |csv|
        csv << %w[numero empresa habilidades]
      end
    end
  end
  
  class EmpresaInfoStackOverflow
    attr_accessor :numero, :empresa, :habilidades
  
    def initialize(numero, empresa, habilidades)
      @numero = numero
      @empresa = empresa
      @habilidades = habilidades
    end
  
    def guardarEmpresaInfoSO(filename)
      CSV.open(filename, 'a+') do |csv|
        csv << [@numero, @empresa, @habilidades]
      end
    end
  end
  
}