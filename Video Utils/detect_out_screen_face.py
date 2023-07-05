import cv2
import dlib
import pyaudio
import wave
import numpy as np

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Inicializar el detector facial y el seguimiento ocular
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Inicializar la grabación de audio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 60

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []

# Inicializar el contador de tiempo
time_counter = 0

# Cargar los puntos de referencia faciales para los ojos
left_eye_points = [36, 37, 38, 39, 40, 41]
right_eye_points = [42, 43, 44, 45, 46, 47]

# Definir una función para calcular la relación de aspecto del ojo (Eye Aspect Ratio o EAR)
def eye_aspect_ratio(eye):
    # Calcular la distancia euclidiana vertical entre los puntos de referencia del ojo
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    # Calcular la distancia euclidiana horizontal entre los puntos de referencia del ojo
    C = np.linalg.norm(eye[0] - eye[3])
    # Calcular la relación de aspecto del ojo
    ear = (A + B) / (2.0 * C)
    return ear

# Bucle principal
while(True):
    # Leer un cuadro de video de la cámara
    ret, frame = cap.read()

    # Convertir el cuadro a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar las caras en el cuadro
    faces = detector(gray)

    # Procesar cada cara detectada
    for face in faces:
        # Obtener los puntos de referencia faciales para la cara
        landmarks = predictor(gray, face)
        landmarks = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)])

        # Obtener los puntos de referencia faciales para los ojos
        left_eye = landmarks[left_eye_points]
        right_eye = landmarks[right_eye_points]

        # Calcular la relación de aspecto de cada ojo
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Calcular la relación de aspecto promedio de los ojos
        ear = (left_ear + right_ear) / 2.0

        # Verificar si la relación de aspecto es menor que un umbral
       
        if ear < 0.2:
            # Si la relación de aspecto es menor que el umbral, el usuario no está mirando a la pantalla
            # Incrementar el contador de tiempo
            time_counter += 1
            # Si el contador de tiempo es mayor que el tiempo de espera deseado, reproducir el sonido de alerta
            if time_counter > 60:
                wf = wave.open("alert.wav", 'rb')
                data = wf.readframes(CHUNK)
                while data != '':
                    stream.write(data)
                    data = wf.readframes(CHUNK)
                wf.close()
                time_counter = 0
        else:
            # Si la relación de aspecto es mayor que el umbral, el usuario está mirando a la pantalla
            # Reiniciar el contador de tiempo
            time_counter = 0

        # Mostrar el cuadro de video en una ventana
        cv2.imshow('frame',frame)

        # Esperar por una tecla para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Detener la grabación de audio
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Liberar la cámara y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()