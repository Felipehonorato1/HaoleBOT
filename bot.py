import telepot
import unidecode
from sendpreview import sendpreview

bot = telepot.Bot('1031484092:AAHfDz4MgkyH3OFbS3qA6HF9GEWqoW4YZyc')


def recebendoMsg(msg):
    chat_id = msg['chat']['id']
    sendpreview(unidecode.unidecode(msg['text'].lower()),chat_id)
     


    if(msg['text'] == '/help'):
         bot.sendMessage(chat_id,'Para ver a previsão do mar nos próximos 7 dias, digite /previsao <sigla do estado> \nex: /previsao pb joao pessoa')

    if(unidecode.unidecode(msg['text'].lower()) == '/previsao'):
        bot.sendMessage(chat_id,'Uso incorreto. \nUse /previsao <sigla do estado>  <cidade>')

                
bot.message_loop(recebendoMsg)


while True:
    pass