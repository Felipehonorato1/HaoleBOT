import cv2
import urllib.request as ulib
import matplotlib.pyplot as plt 
import numpy as np
from datetime import date
## 16 QUADRADOS HORIZONTAIS
## 4 VERTICAIS 260X260

def GetImage(estado):
    c = 0
    i = 0

    if estado == 'rn':
        estado = 'rnLeste'

    ano = int(date.today().year)
    mes = int(date.today().month)
    dia = int(date.today().day)
    ulib.urlretrieve('https://surfguru.pictures/mapas/{}{}{:0>2}{}00.png'.format(estado,abs(ano)%100,mes,dia),'raw.png')
    img = cv2.imread('raw.png')


    start_x = 0
    end_x = 260
    start_y = 0
    end_y = 260
    lista = []

    while end_x <= 4060:
        while end_y <= 1040:
            cropc = img[start_y:end_y,start_x:end_x]
            lista.append(cropc)
            #cv2.imwrite('img{}{}{}{}{}.png'.format(estado,dia+c,mes,ano,i),cropc)
            start_y += 260
            end_y += 260
            i+=1
        c += 1
        start_y = 0
        end_y = 260
        start_x += 520
        end_x += 520
        
    concat = cv2.hconcat([lista[0],lista[1],lista[2],lista[3]])
    cv2.imwrite('img0.png',concat)
    concat = cv2.hconcat([lista[4],lista[5],lista[6],lista[7]])
    cv2.imwrite('img1.png',concat)
    concat = cv2.hconcat([lista[8],lista[9],lista[10],lista[11]])
    cv2.imwrite('img2.png',concat)
    concat = cv2.hconcat([lista[12],lista[13],lista[14],lista[15]])
    cv2.imwrite('img3.png',concat)
    concat = cv2.hconcat([lista[16],lista[17],lista[18],lista[19]])
    cv2.imwrite('img4.png',concat)
    concat = cv2.hconcat([lista[20],lista[21],lista[22],lista[23]])
    cv2.imwrite('img5.png',concat)
    concat = cv2.hconcat([lista[24],lista[25],lista[26],lista[27]])
    cv2.imwrite('img6.png',concat)
    concat = cv2.hconcat([lista[28],lista[29],lista[30],lista[31]])
    cv2.imwrite('img7.png',concat)


    return lista
    
    