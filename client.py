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

# Recepcion de la respuesta
while True:
    rcv_frame = s.recv(Read_Bytes)
    rcv_mensaje = frame_unwrapper(rcv_frame)
    if len(rcv_mensaje):
        print("Trama recibida!")
        logging.debug("Trama recibida\n")
        msg_storage("Rcv_data.txt", rcv_mensaje)
        break
    else:
        print("Esperando Trama ...\n")

# Envio de respuesta
# Codificacion del source y del destination
src = encode_address("TI0TEC", True)
print("Source: TI0TEC-0\n")
dst = encode_address("TI0TEC-1", False)
print("Destination: TI0TEC-1\n\n")
logging.info("Encoded Source: %s\n", str(src))
logging.info("Encoded Destination: %s\n\n", str(dst))

mensaje = "Frame_Correct"   # Acknoledge

# Empaquetado de la trama
frame = frame_wrapper(src, dst, mensaje)
loggign.info("Trama a enviar a traves de KISS: %s\n\n", frame)

# Envio del mensaje
s.send(frame)
print("La trama ha sido enviada\n")
logging.debug("Enviando la trama ...\n")

# Finalizacion de la coneccion KISS
end_kiss()
