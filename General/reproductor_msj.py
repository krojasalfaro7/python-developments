import pyaudio
import socket
import threading
import webbrowser
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def on_connect (cliente, userdata, flags, rc):  # Funcion de devolucion de llamada para conectar.
    client.subscribe ("udp_ip")                 # Topic.

def on_message (client, userdata, msg):         # Funcion de devolucion de llamada para recibir msj.
    global direccion_UDP
    direccion_UDP = msg.payload 

def publicar_chequear():
    
    def on_connect_s (cliente, userdata, flags, rc):  # Funcion de devolucion de llamada para conectar.
        client_s.subscribe ("udp")                      # Topic.
        client_s.subscribe ("parametros")
        
    def on_message_s (client, userdata, msg):         # Funcion de devolucion de llamada para recibir msj.
        musica = msg.payload
        global stream
        if msg.topic == 'udp':
            print ("La peticion requerida es: " + musica.decode())
                
        elif msg.topic == 'parametros':
            valores = musica.decode().split('.')
            formato = int(valores[0])
            canales = int(valores[1])
            frecuencia = int(valores[2])*8000
            stream = p.open(format=formato, channels=canales, rate=frecuencia, output=True)
    
    client_s = mqtt.Client()                  # Creando instancia de cliente
    client_s.on_connect = on_connect_s        # Enlazando funciones de devolucion de llamada para conectar y msj
    client_s.on_message = on_message_s
    client_s.connect (broker)                 # Utilizando el broker de mosquitto.
    client_s.loop_start()
    
    print ("La direccion ip del reproductor es. " + IP_reproductor)
    while True:
        publish.single('reproductor', IP_reproductor, hostname= broker)


def vista_html():
    webbrowser.open_new("file:///C:/Users/KEVINC/Desktop/El%20que%20funciona%20pero%20uno%20solo/UDP_mensajes.html")

    f = open('UDP_mensajes.html','w')

    mensaje_python_2 = """ <html> <center> </body> <p5>La ip del reproductor UDP es: </p5></body> </html>""" + IP_reproductor

    mensaje_prueba = '\n hola de nuevo'
    
    f.write(mensaje_python_2)
    f.write(mensaje_prueba)
    
    f.close()
    
if __name__ == '__main__':

 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    p = pyaudio.PyAudio()
    sock.bind(('', 9999))
    
    broker = '192.168.1.6'
    IP_reproductor = socket.gethostbyname_ex(socket.gethostname())[2][0]
    stream = p.open(format=32, channels=1, rate=8000, output=True)
    hilo = threading.Thread(name='publicar_chequear', target = publicar_chequear)                        
    hilo.start()

    
    client = mqtt.Client()                  # Creando instancia de cliente
    client.on_connect = on_connect          # Enlazando funciones de devolucion de llamada para conectar y msj
    client.on_message = on_message
    client.connect (broker)                 # Utilizando el broker de mosquitto.
    client.loop_start()
    

    #hilo_n = threading.Thread(name='vista_html', target = vista_html)                        
    #hilo_n.start()
    

    while True:                         # Este comando espera a que llegue el msj MQTT,             
        try:                            # Si aun no llega se queda esperando.
            direccion_UDP = direccion_UDP
            break
        except NameError:
            pass
    print ("La direccion ip del UDP server es: " + direccion_UDP.decode())
    
    while True:
        data,addr = sock.recvfrom(4000)
        stream.write(data)
