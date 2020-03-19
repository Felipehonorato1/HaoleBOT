import cv2
import urllib.request as ulib
import matplotlib.pyplot as plt 
import numpy as np
## 16 QUADRADOS HORIZONTAIS
## 4 VERTICAIS 260X260

def GetImage(dia,mes,ano,estado):
    c = 0

    if estado == 'rn':
        estado = 'rnLeste'
    if(ano == 2020):
        ano = 20

    ulib.urlretrieve('https://surfguru.pictures/mapas/{}{}{:0>2}{}00.png'.format(estado,ano,mes,dia),'raw.png')
    img = cv2.imread('raw.png')

    start_y = 0
    end_y = 260
    lista = []

    while end_y <= 1040:
        cropc = img[start_y:end_y,0:260]
        start_y += 260
        end_y += 260
        cv2.imwrite('img{}{}{}{}.png'.format(estado,dia,mes,c),cropc)
        c += 1

    
    