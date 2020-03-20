import requests
from imgsaver import GetImage

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
    path = '/home/felipe/Documentos/surfproject/imgpb273202029.png' 
    params = {"chat_id": chat_id,"photo":path,'caption': 'image'}
    response = requests.post(url + "sendPhoto", data=params)
    return response




def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() ==  "oi" or get_message_text(update).lower() == 'ola':
                send_message(get_chat_id(update),"Eae! Para ver as previsões da sua região digite /previsao estado")
                update_id +=1
            if get_message_text(update).lower() ==  "previsao":
                send_message(get_chat_id(update),"ENVIANDO AS FOTOS FILHO DA PUTA")
                sendImg(get_chat_id(update),'pb')
                update_id +=1
                send_message(get_chat_id(update),"TERMINOU FILHO DA PUTA")
                update_id +=1
            else:
                send_message(get_chat_id(update), "Desculpe, não entendi")
                update_id +=1


main()