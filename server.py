import socket
import sys
import kiss
import logging
import time


logging.basicConfig(filename="Server.log", level=logging.DEBUG)
localtime = time.asctime(time.localtime(time.time()))
logging.info("Log con Fecha %s\n", localtime)

# Inicio de la conexion TCP
s = socket.socket(socket.AF_INEF, socket.SOCK_STREAN)
print("Iniciando la conexion con KISS-TCP ...\n")
s.connect(("127.0.0.1", 8001))
print("Conexion Establecidad con exito\n")

# Codificacion del source y del destination
src = encode_address("TI0TEC-1", True)
print("Source: TI0TEC-1\n")
dst = encode_address("TI0TEC", False)
print("Destination: TI0TEC-0\n\n")
logging.info("Encoded Source: %s\n", str(src))
logging.info("Encoded Destination: %s\n\n", str(dst))

# Extraccion del mensaje a enviar
mensaje = msg_extraction("Data.txt", True)
print("Mensaje:\n %s\n\n",mensaje)
logging.info("Mensaje a enviar: %s\n\n", mensaje)

# Empaquetado de la trama
frame = frame_wrapper(src, dst, mensaje)
loggign.info("Trama a enviar a traves de KISS: %s\n\n", frame)

# Envio del mensaje
s.send(frame)
print("La trama ha sido enviada\n")
logging.debug("Enviando la trama ...\n")

# Recepcion de la respuesta
while True:
    rcv_frame = s.recv(Read_Bytes)
    rcv_mensaje = frame_unwrapper(rcv_frame)
    if rcv_mensaje == "Frame Correct":
        print("La trama ha sido entregada corectamente!\n")
        logging.debug("Trama enviada con exito\n")
        break
    else:
        print("Hubo un problema con la trama, enviar de nuevo\n")
        logging.debug("Envio de la trama fallido\n")

# Finlizacion de la coneccion KISS
end_kiss()

