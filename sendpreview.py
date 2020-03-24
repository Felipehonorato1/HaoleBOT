import telepot
from imgsaver import GetImage
from datacrawler import datacrao
from datetime import date
import os
import glob
bot = telepot.Bot('1031484092:AAHfDz4MgkyH3OFbS3qA6HF9GEWqoW4YZyc')


def sendpreview(msg,chat_id):
    if(msg == '/previsao pb joao pessoa'):
        p = 0
        GetImage('pb')
        dia = int(date.today().day)
        mes = int(date.today().month)
        ano = int(date.today().year)
        previsao = datacrao('paraiba','joao pessoa')
        bot.sendMessage(chat_id,'JOÃO PESSOA:\n')
        for i in range(6):
            bot.sendMessage(chat_id,previsao[i])
            bot.sendPhoto(chat_id,open('img{}.png'.format(i),'rb'))
    
    if(msg == '/previsao rn baia formosa'):
        p = 0
        dia = int(date.today().day)
        mes = int(date.today().month)
        ano = int(date.today().year)
        GetImage('rn')
        previsao = datacrao('rio grande do norte','baia formosa')
        bot.sendMessage(chat_id,'BAIA FORMOSA: \n')
        for i in range(6):
            bot.sendMessage(chat_id,previsao[i])
            bot.sendPhoto(chat_id,open('img{}.png'.format(i),'rb'))
         
    if(msg == '/previsao pe recife'):
        p = 0
        dia = int(date.today().day)
        mes = int(date.today().month)
        ano = int(date.today().year)
        GetImage('pe')
        previsao = datacrao('pernambuco','recife')
        bot.sendMessage(chat_id,'RECIFE: \n')
        for i in range(6):
            bot.sendMessage(chat_id,previsao[i])
            bot.sendPhoto(chat_id,open('img{}.png'.format(i),'rb'))
    
     
    if(msg == '/previsao rn pipa'):
        p = 0
        dia = int(date.today().day)
        mes = int(date.today().month)
        ano = int(date.today().year)
        GetImage('rn')
        previsao = datacrao('rio grande do norte','tibau do sul')
        bot.sendMessage(chat_id,'PIPA: \n')
        for i in range(6):
            bot.sendMessage(chat_id,previsao[i])
            bot.sendPhoto(chat_id,open('img{}.png'.format(i),'rb'))


    directory='/home/felipe/Documentos/surfproject/'
    os.chdir(directory)
    files=glob.glob('*.png')
    for filename in files:
        os.unlink(filename)