import telepot
from imgsaver import GetImage
from datacrawler import datacrao
from datetime import date

bot = telepot.Bot('1031484092:AAHfDz4MgkyH3OFbS3qA6HF9GEWqoW4YZyc')


def recebendoMsg(msg):
    chat_id = msg['chat']['id']
    if(msg['text'] == '/previsao pb' or msg['text'] == '/previsao PB' or msg['text'] == '/previsao Pb'):
        p = 0
        GetImage('pb')
        dia = int(date.today().day)
        mes = int(date.today().month)
        ano = int(date.today().year)
        previsao = datacrao('paraiba','joao pessoa')
        bot.sendMessage(chat_id,'PARAÍBA:\n')
        for i in range(6):
            bot.sendMessage(chat_id,previsao[i])
            bot.sendPhoto(chat_id,open('img{}.png'.format(i),'rb'))
    
    if(msg['text'] == '/previsao rn' or msg['text'] == '/previsao RN' or msg['text'] == '/previsao Rn'):
        p = 0
        dia = int(date.today().day)
        mes = int(date.today().month)
        ano = int(date.today().year)
        GetImage('rn')
        previsao = datacrao('rio grande do norte','baia formosa')
        bot.sendMessage(chat_id,'RIO GRANDE DO NORTE: \n')
        for i in range(6):
            bot.sendMessage(chat_id,previsao[i])
            bot.sendPhoto(chat_id,open('img{}.png'.format(i),'rb'))
     
    if(msg['text'] == '/help'):
         bot.sendMessage(chat_id,'Para ver a previsão do mar nos próximos 7 dias, digite /previsao <sigla do estado> \nex: /previsao pb')

    if(msg['text'] == '/previsao'):
        bot.sendMessage(chat_id,'Uso incorreto. \nUse /previsao <sigla do estado> ')

                
bot.message_loop(recebendoMsg)


while True:
    pass