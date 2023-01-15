# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot("733599470:AAEZVFBj5rUP5828Qd5wQ-TpP9eyyBxj2-U")

@bot.message_handler(commands=['start']) #Si se envia un comando
def send_welcome(message):    
	bot.reply_to(message, "Hola, ¿cómo estás?, ¿eres KEVIN ROJAS?")

@bot.message_handler(commands=['help'])
def send_welcome(message):    
	bot.reply_to(message, "Esta es la ayuda")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if (message.text == "kevin"):
		bot.reply_to(message, "Eres Kevin Rojas :D")

	else:
		bot.reply_to(message, "Me mandaste esto -> " + message.text)


if __name__ == "__main__":

    print ("Iniciando...")
    bot.polling()
    print ("Terminado...")
