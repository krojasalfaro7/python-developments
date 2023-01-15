# -*- coding: utf-8 -*-

import threading      #Para multiprocesos
import os             #Para crear un archivo txt y controlar la ejecucion de los hilos
import telebot
import urllib.request


############################################################# BOT #######################################################################################
bot = telebot.TeleBot("1029732734:AAEFTvm27goRfuYF5nnfW1rvD86Ye5EljBM")

@bot.message_handler(commands=['start']) #Si se envia un comando
def send_welcome(message):
	bot.reply_to(message, "Hola, ¿cómo estás? este es el Bot de edooit para la comunicación con el canal de Chat Web de odoo")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Esta es la ayuda")

"""@bot.message_handler(commands=['poweroff'])
def send_welcome(message):
	#os.system("poweroff")
        bot.reply_to(message, "Apagando pc...")
	#os.system('poweroff')"""

"""@bot.message_handler(commands=['reboot'])
def send_welcome(message):
	#os.system("reboot")
        bot.reply_to(message, "Reiniciando pc...")
	#os.system('reboot')"""


@bot.message_handler(commands=['ip'])
def send_welcome(message):
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	bot.reply_to(message, "Esta es la IP Pública: \n" + ip)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if (message.text == "Kevin"):
		bot.reply_to(message, "Eres Kevin Rojas :D")

	elif (message.text == "Antonio"):
                bot.reply_to(message, "Eres Antonio Rojas :D")

	elif (message.text == "Mireila"):
                bot.reply_to(message, "Eres Mireila Alfaro :D")

	else:
		f = open('ordenar', 'w')
		h = open('listaordenadaE', 'w')
		g = open('listaordenada', 'r')
		f.write(message.text)
		f.close()
		os.system("sort ordenar > listaordenada")
                #for linea in g:
		for linea in g:
                    h.write(linea)
                    h.write('\n')
		h.close()
		h = open('listaordenadaE','r')
		g.close()
		lista_ordenada = h.read()
		h.close()
		bot.reply_to(message, lista_ordenada)

		#bot.reply_to(message, "Me mandaste esto -> " + message.text)

#########################################################################################################################################################

########################################THREADS############################################################

class MiThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("HOLA SOY EL HILO")

###########################################################################################################

if __name__ == "__main__":

    print ("Iniciando bot...")
    bot.polling()
