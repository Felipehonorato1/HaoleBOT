from selenium import webdriver
import pandas as pd 
import requests
import cv2

def datacrao(estado,cidade):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    swell = False
    path = "/home/felipe/Documentos/surfproject/chromedriver"
    driver = webdriver.Chrome(path,options=options)
    for j in range(len(estado)):
        if estado[j] == ' ':
            estado = estado[:k] + '-' +estado[k+1:]
    for k in range(len(cidade)):
        if cidade[k] == ' ':
            cidade = cidade[:k] + '-' +cidade[k+1:]

    url = "https://www.surfguru.com.br/previsao/brasil/" + estado + "/" + cidade + "?tipo=tabela"
    print(url)
    driver.get(url)

    dias = []
    alturas = []
    periodos = []
    dirs_primarias = []
    nos = []
    dir_vento = []
    previsao = []
    carne = []

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

        carne = 'DATA: '+ dias[i-1] + '\nALTURA: '+ alturas[i-1] + '\nPERIODOS: ' + periodos[i-1] + ' \nDIRECOES PRIMARIAS: ' + dirs_primarias[i-1] +  ' \nNOS: ' + nos[i-1] + ' \nDIRECOES DO VENTO: ' + dir_vento[i-1]
        previsao.append(carne.upper())
        # carne = [dias[i-1],alturas[i-1],dirs_primarias[i-1],nos[i-1],dir_vento[i-1],carne[i-1]]
        # previsao.append(carne)

    # ids interessados ssat2 sspp2 ssdp2 ssv2 ssd2
    #//*[@id="rotulo_sem_1_1"]
    #//*[@id="rotulo_sem_1_3"]
    #//*[@id="rotulo_sem_1_2"]
    driver.close()
    return previsao


# df = pd.DataFrame({'Dia ':dias, 'Periodos':periodos,'Alturas':alturas,'Nós':nos })
# df.to_csv('mareview.csv',index=False,encoding='utf-8')
# driver.close()


