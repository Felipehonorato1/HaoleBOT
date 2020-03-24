import requests
from imgsaver import GetImage
from datacrawler import datacrao
import telepot 
import sys
bot = telepot.Bot('1031484092:AAHfDz4MgkyH3OFbS3qA6HF9GEWqoW4YZyc')

url = "https://api.telegram.org/bot1031484092:AAHfDz4MgkyH3OFbS3qA6HF9GEWqoW4YZyc/"

def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id

def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result)-1
    return result[total_updates]

def send_message(chat_id,message_text):
    params = {"chat_id": chat_id, "text":message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

def sendImg(chat_id,estado):
    
    #path = '/home/felipe/Documentos/surfproject/imgpb2732202017.png'
    fp = open('./imgpb263202014.png','rb')
    if(fp):
        print("PELO MENOS EU ABRI A IMAGEM IRMAO")
    params = {"chat_id": chat_id, "photo":fp}
    response = requests.post(url + "sendPhoto", data=params)
    return response




def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() ==  "oi" or get_message_text(update).lower() == 'ola':
                previsao = datacrao('paraiba','joao pessoa')
                send_message(get_chat_id(update),'**PREVISAO PORRA**')
                update_id +=1
                for i in range(6):
                    send_message(get_chat_id(update),previsao[i])
                    bot.sendPhoto(get_chat_id(update),open('imgpb233{i}.png','rb'))
                    update_id +=1
                    sendImg(get_chat_id,'pb')
                    update_id +=1




            # if get_message_text(update).lower() ==  "/previsao":
            #     send_message(get_chat_id(update),"ENVIANDO AS FOTOS FILHO DA PUTA")
            #     sendImg(get_chat_id(update),'pb')
            #     update_id +=1
            #     send_message(get_chat_id(update),"TERMINOU FILHO DA PUTA")
            #     update_id +=1

main()