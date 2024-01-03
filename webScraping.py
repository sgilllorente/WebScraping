import requests
from bs4 import BeautifulSoup

def get_current_price():
    url = requests.get('https://www.eneba.com/es/logitech-g27-like-g29-g923-g920-g25-f7a005f3') 
    soup = BeautifulSoup(url.text, 'html.parser')
    result = soup.find('span', class_ ='L5ErLT dXrfjQ') 

    price_text= result.text
    price_text = price_text.replace("€","")
    price_text = price_text.replace(",",".")
    
    main_price = float(price_text)
    return main_price
    
