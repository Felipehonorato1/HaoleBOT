import cv2
import urllib.request as ulib
import matplotlib.pyplot as plt 
import numpy as np
from datetime import date
## 16 QUADRADOS HORIZONTAIS
## 4 VERTICAIS 260X260

def GetImage(estado,prev):
    c = 0

    if estado == 'rn':
        estado = 'rnLeste'

    ano = int(date.today().year)
    mes = int(date.today().month)
    dia = int(date.today().day)

    ulib.urlretrieve('https://surfguru.pictures/mapas/{}{}{:0>2}{}00.png'.format(estado,abs(ano)%100,mes,dia),'raw.png')
    img = cv2.imread('raw.png')


    start_x = 520*prev
    end_x = start_x + 260
    start_y = 0
    end_y = 260

    while end_y <= 1040:
        cropc = img[start_y:end_y,start_x:end_x]
        start_y += 260
        end_y += 260
        cv2.imwrite('img{}{}{}{}{}.png'.format(estado,dia+prev,mes,ano,c),cropc)
        c += 1

    
    