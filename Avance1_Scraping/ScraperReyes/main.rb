# Scraper para usuarios de StackOverflow
# Reyes Medranda Diego Javier
# Avance 1

require 'open-uri' # consultar a la plataforma
require 'nokogiri' # formatear, parsear a html
require 'csv' # escribir y leer csv

#Clase "Usuario" para guardar los datos

class Usuario

  attr_accessor :nombre, :link, :pais, :reputacion, :n_oro, :n_plata, :n_bronce
  
  def initialize(nombre, link, pais, reputacion, n_oro, n_plata, n_bronce)
    @nombre = nombre
    @link = link
    @pais = pais
    @reputacion = reputacion
    @n_oro = n_oro
    @n_plata = n_plata
    @n_bronce = n_bronce
  end
    #Metodo para guardar los datos del scraping en archivo 'users.csv'
   def guardar()
    CSV.open('users.csv', 'a') do |csv|
      csv << [@nombre, @link, @pais, @reputacion, @n_oro, @n_plata, @n_bronce]
    end
  end
end
#Se añade cabecera al archivo 'users.csv'
CSV.open('users.csv', 'wb') do |csv|
  csv << %w[Nombre Link Pais Reputacion N_oro N_plata N_bronce]
end
#Variables para controlar la cantidad de usuarios que se guardan y navegar
#a través de las paginas del link (cantidad de usuarios puede
#variar para guardar más registros de ser necesario)
usuario = 0; page = 1

  while(usuario < 400) 
    link = "https://stackoverflow.com/users?page=#{page}&tab=reputation&filter=all"
    puts "Impresión de datos de scraping\n"
    puts "........................................................."
    pagina = URI.open(link)
    contenido = Nokogiri::HTML(pagina.read)
    contenedor = contenido.css('.d-grid.grid__4')

    contenedor.css('.grid--item.user-info').each do |datos|
     nombre = datos.css('.user-details').css('a').inner_text
     puts "Nombre de Usuario: "+nombre

     link = datos.css('.user-details').css('a').attribute("href").inner_text
     link = 'https://stackoverflow.com' + link
     puts "Link: "+link

     pais = datos.css('.user-details').css('.user-location').inner_text.gsub(",",";")
      if pais==""
        pais= "Not provided by the user"
      end
     puts "Pais/Locación: "+pais

     reputacion = datos.css('.user-details').css('.reputation-score').attribute('title').to_s.split(" ")[2].gsub(",","")
     puts "Reputación: "+reputacion  

     medallas = ""
     medals = datos.css('.user-details').css('.badgecount').each do |med|  
       medallas+=med.inner_text.to_s
       medallas+="-"
     end
     medallas = medallas.gsub("-"," ").strip
     oro=medallas.split(" ")[0].to_s
     plata=medallas.split(" ")[1].to_s
     bronce=medallas.split(" ")[2].to_s
     puts "# medallas de oro: "+oro
     puts "# medallas de plata: "+plata
     puts "# medallas de bronce: "+bronce

     user = Usuario.new(nombre, link, pais, reputacion, oro, plata, bronce)
     user.guardar()
     puts "------------------------------------------------------------"
     usuario+=1
    end
    page+=1
  end
