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
            cv2.imwrite('img{}{}{}{}{}.png'.format(estado,dia+c,mes,ano,i),cropc)
            start_y += 260
            end_y += 260
            i+=1
        c += 1
        start_y = 0
        end_y = 260
        start_x += 520
        end_x += 520

    return lista
    
    