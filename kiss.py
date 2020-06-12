
import socket
import time
import sys

# Constantes
Fend = 0xC0     # Bandera de inicio y final de trama
Fesc = 0xDB     # Caracter de escape
# Si en el mensaje hay un Fend se debe cambiar por un FescTFend, si se recibe 
# despues de un Fesc se debe sustituir por un Fend
TFend = 0xDC
# Si en el mensaje hay un Fesc se debe cambiar por un FescTFesc, si se recibe
# despues de un Fesc se debe sustituir por un Fesc
TFesc = 0xDD
Type_Frame = 0x03   # Indicador de trama UI
PID = 0xF0          # Indicador sin protocolo de 3ra capa
Send_Data = 0x00    # Comando para indicar a Kiss un envio de datos

read_buffer = bytes()

# Funcion para recuperar caracter en escape
def recover_characters(code):
    return code.replace([Fesc, TFes], Fesc).replace([[Fesc, TFend], Fend)

def encode_address(address, final):
    if "-" not in s:
        address = address + "-0"
    callsign, ssid = address.split("-")
    if len(callsign) < 6:
        if len(callsign) < 6:
            sys.exit("Callsign Incorrecto")
        encoded_callsign = [ord(c) << 1 for c in callsign]
        encoded_ssid = (int(ssid) << 1) | 0b01100000 | (0b00000001 if final else 0)
        return encoded_callsign + [encoded_ssid]


def msg_extraction(Filename, All):
    File = open(Filename, "r")
    contador = 1
    if All:
        message = File.read()
    else:
        for linea in File:
            message(1) = linea
    File.close()
    return message

def msg_storage(Filename, msg):
    File = open(Filename, "w")
    File.write(msg)
    File.close()

def frame_wrapper(source, destination, message):
    frame = destination + source + [Type_Frame] + [PID] + message
    # Si hay un caracter de escape se debe reemplazar por el caracter
    # correspondiente
    packet = []
    for caracter in frame:
        if caracter == Fend:
            packet += [Fesc, TFend]
        elif caracter == Fesc:
            packet += [Fesc, TFesc]
        else:
            packet += [caracter]
    kiss_frame = [Fend, Send_Data] + packet + [Fend]
    return str(bytearry(kiss_frame))    # Retorna la trama a enviar

def frame_unwrapper(frame):
    if frame is not None and len(frame):
        data = []
        # Cuenta los fends en la trama
        split_data = frame,split(Fend)
        fends = len(split_data)

        if fends == 1:
            read_buffer += split_data[0]
        
        elif fends == 2:
            # Continua trama parcial, sino se desecha
            if split_data[0]:
                data.append(b''.join([read_buffer, split_data[0]]))
                read_buffer = bytes()
            else:
                data.append(read_buffer)
                read_buffer = split.data[1]
        # Al menos una trama recibida
        elif fends >= 3:
            for i in range(0, fends-1):
                buff = bytearray(b''.join([read_buffer], split_data[i]))
                if buff:
                    data.append(buff)
                    read_buffer = bytearray()

            if split_data[fends-1]:
                read_buffer = bytearray(split_data[fends-1])
        data = list(map(recover_character, data))

        return data

def end_kiss():
    end_frame = b''.join([Fend, [0xFF], Fend])
    s.send(end_frame)
    s.close()
