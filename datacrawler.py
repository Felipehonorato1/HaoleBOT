#from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd 
import requests

url = "https://www.surfguru.com.br/previsao/brasil/paraiba/joao-pessoa?tipo=tabela"

html = requests.get(url)
if html.status_code == 200:
    print('Requisicao bem sucedida!')
    content = html.content

#path = "/home/felipe/Documentos/surfproject/chromedriver"
#driver = webdriver.Chrome(path)
#driver.get("https://www.surfguru.com.br/previsao/brasil/paraiba/joao-pessoa?tipo=tabela")
#content = driver.page_source

res = BeautifulSoup(content,"html.parser")
results = res.find(id="ssat1")

print("Message: {}".format(results.prettify()))
# ids interessados ssat2 sspp2 ssdp2 ssv2 ssd2


#df = pd.DataFrame({'Dia ':dia, })
