import requests
from bs4 import BeautifulSoup


url = requests.get('https://www.eneba.com/es/logitech-g27-like-g29-g923-g920-g25-f7a005f3') 

soup = BeautifulSoup(url.text, 'html.parser') # aquí estamos parseando la página web, es decir, analizamos el contenido del url

result = soup.find('span', class_ ='L5ErLT dXrfjQ') ##soup.find("span", {"class":"a-price-whole"}) 


price_text= result.text
price_text = price_text.replace("€","")
price_text = price_text.replace(",",".")
#print(price_text)

main_price = float(price_text)

##condicion -> En este caso quiero que me avise el bot cuando el precio sea menor que 149.99
flat_price = main_price +1

'''
if main_price < flat_price:
    print("Hay oferta")
else:
    print("No hay oferta")
'''