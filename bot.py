import time
import requests
from webScraping import main_price
from webScraping import flat_price


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

while True:
    

    # Comparar con el precio fijo y aplicar el umbral de cambio
    if main_price < flat_price +1:
        mensaje = f"¡El precio ha bajado! Está en: {str(main_price) + '€'}\n\nEnlace: https://www.eneba.com/es/logitech-g27-like-g29-g923-g920-g25-f7a005f3"
        telegram_bot_sendtext(mensaje)
        print(mensaje)  # Agregar un mensaje para depuración
        flat_price = main_price

        

    # Esperar 60 segundos antes de revisar nuevamente
    time.sleep(30)

