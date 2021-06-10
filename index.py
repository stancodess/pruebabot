import telebot # Importamos las librería
import requests
import json
TOKEN = "1835557133:AAFRjJ6hR-Psn6QK1Z44KPhLXOcLeJ_5EM0" # Ponemos nuestro Token generado con el @BotFather
bot = telebot.TeleBot(TOKEN)  #Creamos nuestra instancia "bot" a partir de ese TOKEN










@bot.message_handler(commands=['bgp'])
def send_welcome(message):
    bot.reply_to(message, "¿Me ha llamado maestro sensei?")
    bot.reply_to(message, "Ejecutando el APi")

    print("SOLICITANDO INFORMACION DE INTERNET")
    print("espere....")
    URL = 'http://127.0.0.1:5000/pruebaApi' #configuramos la url
    payload = { 'red': '181.39.24.204' }
    #solicitamos la información y guardamos la respuesta en data.
    data = requests.post(URL, json=payload)
    #print( data.content.decode() )
    text = json.loads(data.content.decode())
    #data = data.json() #convertimos la respuesta en dict
    f = open('gpb.txt', 'wb')
    f.write( text["data"].encode('ascii') )
    f.close()
    doc = open('gpb.txt', 'rb')
    bot.send_document( -568931818, doc )
    
    #bot.reply_to(message, text["data"] )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()