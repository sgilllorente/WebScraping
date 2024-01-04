# WebScraping
En este proyecto, se desarrollaron dos programas en Python con el propósito de realizar un seguimiento automatizado de los precios de productos en la página web de Eneba.com, en específico un volante de simulación de carreras.

El proyecto se resume en dos programas en python, uno para ralizar el webscraping del sitio web, y el otro para crear y configurar el bot de telegram. A continuación se detalla cada uno de ellos.

## Programa para WebScraping [(ver programa)](https://github.com/sgilllorente/WebScraping/blob/main/webScraping.py)

En este programa se tiene la función "get_current_price()" donde se selecciona el enlace al artículo de interés, puede ser cualquier artículo de cualquier página.

      url = requests.get('https://www.eneba.com/es/logitech-g27-like-g29-g923-g920-g25-f7a005f3') 
      soup = BeautifulSoup(url.text, 'html.parser')
      result = soup.find('span', class_ ='L5ErLT dXrfjQ')

Parseamos en enlace y filtramos por clase (class_ ='L5ErLT dXrfjQ') y por etiqueta ('span'). Estos parámetros dependerán de la web y el producto que queramos scrapear.
Por último realizamos algún filtrado del valor obtenido, como elimiar el '€' y cambiar la coma por punto decimal. Finalmente devolvemos en la función el valor final con el que trabajará el programa del bot.

## Programa para bot de telegram [(ver programa)](https://github.com/sgilllorente/WebScraping/blob/main/bot.py)

En este programa tenemos la función que configura y el bot para la comunicación y un bucle infinito para que constantemete se compruebe el precio del artículo.

      def telegram_bot_sendtext(bot_message):
          bot_token = ''
          bot_chatID = ''
          send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
      
          response = requests.get(send_text)
      
          return response.json()

Deberemos introducir el token de nuestro bot en "bot_token" y el id de nuesto bot en "bot_chatID". Podremos crear nuestro bot haciendo uso de [BotFather](https://telegram.me/BotFather) 
