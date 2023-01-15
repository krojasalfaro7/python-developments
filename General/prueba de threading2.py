#================================================================================================
#                                  Servidor UDP-Streaming
#================================================================================================

#==============
# Bibliotecas
#==============
import socket  
import wave, struct
import os
import threading
import time
import urllib
import urllib.request, urllib.parse, urllib.error
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from pydub import AudioSegment
#======================
# Fin de importaciones
#======================

#=====================================
# Funciones MQTT - Programa Principal
#=====================================
def on_connect (cliente, userdata, flags, rc):  # Funcion de devolucion de llamada para conectar.
    client.subscribe ("udp")                    # Topic del UDP.

def on_message (client, userdata, msg):         # Funcion de devolucion de llamada para recibir msj.
    global mensaje
    mensaje = msg.payload                       # Guarda el valor de la variable recibida en mensaje.
#=========================================
# Fin funciones MQTT - Programa Principal
#=========================================


#=========================================================================
# Funciones para convertir formatos de audio y envio - Programa Principal
#=========================================================================
def convertidor(nombre_archivo):                # Funcion que permite convertir un archivo .WAV 8Khz, 8bits a muestras PCM
    global waveFile
    global length
    nombre_archivo = nombre_archivo + "wav"
    directorio = 'C:\\Users\\kevin\\Desktop\\audios\\'      # CAMBIAR EL DIRECTORIO A USAR EN WEB2PY
    waveFile = wave.open(directorio + nombre_archivo, 'rb') # Se van a abrir los archivos que esten en esa carpeta
    length = waveFile.getnframes()
    
def revisar():                                              # Rutina que revisa si el archivo tiene extenxion .wav
    global error
    wav = int(7823734)
    mensaje_r = mensaje                                     # Si no la tiene lo convierte, 
    mensaje_r = mensaje_r[len(mensaje_r)-3:]                # Solo se queda con la extenxion 
    mensaje_r = int.from_bytes(mensaje_r, byteorder = 'big')# Para convertir la cadena byte a int
    if (mensaje_r - wav) != 0:
        global directorio
        directorio = 'C:\\Users\\kevin\\Desktop\\audios\\'
        mensaje_n = mensaje
        mensaje_3 = mensaje[len(mensaje)-3:]
        if mensaje_3 == b'mp3':
            sound_mp3 = AudioSegment.from_mp3(directorio + '\\' + mensaje_n.decode())
            sound_mp3.export(directorio + '\\' + mensaje_n.decode()[:len(mensaje)-3] + 'wav', format="wav")
            mensaje_l = mensaje.decode()[:len(mensaje)-3]

        elif mensaje_3 == b'ogg':
            sound_ogg = AudioSegment.from_ogg(directorio + '\\' + mensaje_n.decode())
            sound_ogg.export(directorio + '\\' + mensaje_n.decode()[:len(mensaje)-3] + 'wav', format="wav")
            mensaje_l = mensaje.decode()[:len(mensaje)-3]    
        else:
            print('no se encuentra el audio requerido')
            error = b'error'
    else:
        mensaje_l = mensaje.decode()[:len(mensaje)-3]
        
def enviar():
    print (length)
    fragmento = length/1000
    fragmento = int(fragmento)+2
    direcciones = ('192.168.1.2', '192.168.1.9', '192.168.1.20', '192.168.1.19')
    for i in range(0, fragmento):
        datos = waveFile.readframes(1000)
        for i in range(0, len(direcciones)):
            addr = (direcciones[i], 9999)
            s.sendto(datos, addr)
        time.sleep(0.09999996942749023)
#=============================================================================
# Fin funciones para convertir formatos de audio y envio - Programa Principal
#=============================================================================

#=====================
# Programa Secundario
#=====================
def chequear():
#======================================
# Funciones MQTT - Programa Secundario
#======================================
    def on_connect_s (cliente, userdata, flags, rc):  # Funcion de devolucion de llamada para conectar.
        client_s.subscribe ("reproductor")                    # Topic del UDP.

    def on_message_s (client, userdata, msg):         # Funcion de devolucion de llamada para recibir msj.
        mensaje_s = msg.payload                       # Guarda el valor de la variable recibida en mensaje.
        print('esteeeeeeeeeeeeeeeeeeeeeeeee ' + mensaje_s.decode())     
#==========================================
# Fin funciones MQTT - Programa Secundario
#==========================================


#=======================================
# Inicio del Main - Programa secundario
#=======================================
    client_s = mqtt.Client()                  # Creando instancia de cliente
    client_s.on_connect = on_connect_s          # Enlazando funciones de devolucion de llamada para conectar y msj
    client_s.on_message = on_message_s
    client_s.connect (broker)   # Utilizando el broker de mosquitto.
    client_s.loop_start()
    while True:                         # Este comando espera a que llegue el msj MQTT,             
        publish.single('udp_ip', IP_UDP, hostname= broker)
#=====================================
# Fin del Main - Programa Secuandario
#=====================================
#============================
# Fin de Programa Secundario
#============================



#====================================
# Inicio del Main - Programa General
#====================================
if __name__ == '__main__':

    global direcciones
    IP_UDP = socket.gethostbyname_ex(socket.gethostname())[2][0]
    broker = 'test.mosquitto.org'
    publish.single('udp_ip', IP_UDP, hostname= broker)
    
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Asignando socket para conexion UDP
    s.bind((IP_UDP,9999))
    # Este comando es para descargar las muestras por stremaing de la radio
    f_streaming = urllib.request.urlopen("http://eu.cdn.egostreaming.com:8000/;stream.mp3")
    
    client = mqtt.Client()                  # Creando instancia de cliente
    client.on_connect = on_connect          # Enlazando funciones de devolucion de llamada para conectar y msj
    client.on_message = on_message
    client.connect (broker)   # Utilizando el broker de mosquitto.
    client.loop_start()
    
    hilo = threading.Thread(name='chequear', target=chequear)                         
    hilo.start()
    
    while True:                             # El servidor UDP se queda mandando constantemente.
        while True:                         # Este comando espera a que llegue el msj MQTT,             
            try:                            # Si aun no llega se queda esperando. 
                mensaje = mensaje
                break
            except NameError:
                publish.single('udp_ip', IP_UDP, hostname= broker)
                
        print("la peticion recibida es: " + mensaje.decode())
        
        if mensaje == b'streaming':
            Muestras_audio_streaming = f_streaming.read(1000)
            direcciones = ('192.168.1.2', '192.168.1.9', '192.168.1.20', '192.168.1.19')
            for i in range(0, fragmento):
                datos = waveFile.readframes(1000)
                for i in range(0, len(direcciones)):
                    addr = (direcciones[i], 9999)
                    s.sendto(Muestras_audio_streaming, addr)
                time.sleep(0.09999996942749023)
        
        else:                               # Revisa si la musica requerida esta en formato .wav
            error = b'-'
            revisar()                                # Si no lo esta lo convierte a ese formato y lo conveirte a PCM
            if error != b'error':
                audio = mensaje.decode()[:len(mensaje)-3] # Convierte el bytes en string
                convertidor(audio)              # Convierte el audio .wav a codificacion PCM
                enviar()                        # Envia los datos de audio al ESP8266

            time.sleep(2)
#=================================
# Fin del Main - Programa General
#=================================


#===============
# Comentarios
#===============
##elif data == b'transmision':
##Este codigo es para descargar el MP3 de cualquier servidor pregrabados falta por trabajar"
##Proximamente realizar el script para grabar audio en tiempo real y pasarlo por las cornetas
#estilo el streming de la radio pero personal..
#urllib.request.urlretrieve("http://eu.cdn.egostreaming.com:8000/;stream.mp3", "stream.mp3")
#=================
# Fin Comentarios
#=================
