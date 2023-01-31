puts "Scraper de StackOverflow en relación a los tags \u{1f3ac}"

require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv

# Añadiendo cabecera a pregunta1.csv
CSV.open('datasetGV.csv', 'w') do |csv|
  csv << %w[Anio Tag]
  header = %w[Anio Tag]
end

numero_pagina = 1

link1 = "https://stackoverflow.com/questions/tagged/javascript?tab=frequent&page=#{numero_pagina}&pagesize=50"
link2 = "https://stackoverflow.com/questions/tagged/python?tab=frequent&page=#{numero_pagina}&pagesize=50"
link3 = "https://stackoverflow.com/questions/tagged/java?tab=frequent&page=#{numero_pagina}&pagesize=50"
link4 = "https://stackoverflow.com/questions/tagged/c?tab=frequent&page=#{numero_pagina}&pagesize=50"
link5 = "https://stackoverflow.com/questions/tagged/php?tab=frequent&page=#{numero_pagina}&pagesize=50"
link6 = "https://stackoverflow.com/questions/tagged/android?tab=frequent&page=#{numero_pagina}&pagesize=50"
link7 = "https://stackoverflow.com/questions/tagged/html?tab=frequent&page=#{numero_pagina}&pagesize=50"
link8 = "https://stackoverflow.com/questions/tagged/jquery?tab=frequent&page=#{numero_pagina}&pagesize=50"
link9 = "https://stackoverflow.com/questions/tagged/c%2b%2b?tab=frequent&page=#{numero_pagina}&pagesize=50"
link10 = "https://stackoverflow.com/questions/tagged/css?tab=frequent&page=#{numero_pagina}&pagesize=50"
arrayLink = [link1, link2, link3, link4, link5, link6, link7, link8, link9, link10]

arrayLink.each do |link|
  while numero_pagina <= 5
    pagina = URI.open(link)
    paginaParsed = Nokogiri::HTML(pagina.read)

    container_nombre = paginaParsed.css('.d-flex').css('.fl1').css('.flex--item').inner_text.split(' ')[7]
    puts paginaParsed.css('.d-flex').css('.fl1').css('.flex--item').inner_text.split(' ')[7]

    general_Container = paginaParsed.css('.flush-left')
    general_Container.css('.s-post-summary').each do |pregunta|
      titulo_pregunta = pregunta.css('.s-post-summary--content').css('.s-post-summary--content-title').css('a').inner_text

      if !pregunta.css('.s-post-summary--content').css('.s-post-summary--meta').css('.s-user-card').css('.s-user-card--time').css('.relativetime').inner_text.split(',')[1].nil?
        anio = pregunta.css('.s-post-summary--content').css('.s-post-summary--meta').css('.s-user-card').css('.s-user-card--time').css('.relativetime').inner_text.split(',')[1]
      else
        anio = 'n/a'
      end

      puts paginaParsed.css('.d-flex').css('.fl1').css('.flex--item').inner_text.split(' ')[7]

      class Pregunta
        def initialize(anio, tag)
          # atributos
          @anio = anio
          @tag = tag
        end

        # Getters

        attr_reader :anio

        attr_reader :tag

        # Setters

        attr_writer :anio

        attr_writer :tag

        def guardar
          CSV.open('datasetGV.csv', 'a') do |csv|
            # csv << %w[Pregunta Anio]
            csv << [@anio.to_s, @tag.to_s]
          end
        end
      end

      preg = Pregunta.new(anio, container_nombre)
      preg.anio = if preg.anio == ''
                    'n/a'
                  else
                    preg.anio[1, 4]
                  end
      preg.guardar
    end
    numero_pagina += 1
  end
  numero_pagina = 1
end
