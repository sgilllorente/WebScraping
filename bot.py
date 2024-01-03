import time
import requests
from webScraping import get_current_price

previous_price = None

def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

while True:
    

    # Comparar con el precio fijo y aplicar el umbral de cambio
    current_price = get_current_price()
    print(current_price)
    
    if previous_price is not None and current_price < previous_price:
        mensaje = f"¡El precio ha bajado! Está en: {str(current_price) + '€'}\n\nEnlace: https://www.eneba.com/es/logitech-g27-like-g29-g923-g920-g25-f7a005f3"
        telegram_bot_sendtext(mensaje)
        print(mensaje)  # Agregar un mensaje para depuración
        
    previous_price = current_price   
    # Esperar 60 segundos antes de revisar nuevamente
    time.sleep(30)

