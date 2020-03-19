from selenium import webdriver
import pandas as pd 
import requests
import cv2


options = webdriver.ChromeOptions()
options.add_argument('headless')

path = "/home/felipe/Documentos/surfproject/chromedriver"
driver = webdriver.Chrome(path,options=options)
driver.get("https://www.surfguru.com.br/previsao/brasil/rio-grande-do-norte/baia-formosa?tipo=tabela")

dias = []
alturas = []
periodos = []
dirs_primarias = []
nos = []
dir_vento = []


for i in range(1,7):
    xpathday = '//*[@id="rotulo_sem_1_{}"]'.format(i)
    xpathssat = '//*[@id="ssat{}"]'.format(i)
    xpathsspp = '//*[@id="sspp{}"]'.format(i)
    xpathssdp = '//*[@id="ssdp{}"]'.format(i)
    xpathssv1 = '//*[@id="ssv{}"]'.format(i)
    xpathssd1 = '//*[@id="ssd{}"]'.format(i)

    dias.append(driver.find_element_by_xpath(xpathday).text)
    alturas.append(driver.find_element_by_xpath(xpathssat).text)
    periodos.append(driver.find_element_by_xpath(xpathsspp).text)
    dirs_primarias.append(driver.find_element_by_xpath(xpathssdp).text)
    nos.append(driver.find_element_by_xpath(xpathssv1).text)
    dir_vento.append(driver.find_element_by_xpath(xpathssd1).text)

# ids interessados ssat2 sspp2 ssdp2 ssv2 ssd2
#//*[@id="rotulo_sem_1_1"]
#//*[@id="rotulo_sem_1_3"]
#//*[@id="rotulo_sem_1_2"]
df = pd.DataFrame({'Dia ':dias, 'Periodos':periodos,'Alturas':alturas,'Nós':nos })
df.to_csv('mareview.csv',index=False,encoding='utf-8')
driver.close()


