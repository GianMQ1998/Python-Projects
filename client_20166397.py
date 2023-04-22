#Alumno: Mamani Quispe Gian Carlos
# Codigo: 20166397
from pickle import FALSE
import socket
import time


SOCK_BUFFER = 65536

SLEEP_TIME = 1

if __name__ == '__main__':
    # crea el objeto de socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5020)
    print(f"Conectando a servidor -> {server_address[0]}, en el puerto -> {server_address[1]}")
    # Se conecta a la direccion del servidor
    sock.connect(server_address)
    # Variable enable que permitira establecer un bucle que mantenga el servidor activo mientas no se envie en mensaje de cerrar sesion
    enable=True

    while enable:
        try:
            msg = input("Ingrese comando: ")
            msg = msg.encode('utf8')
            sock.sendall(msg)
            time.sleep(SLEEP_TIME)

            data = sock.recv(SOCK_BUFFER)                
            msg_rx = data.decode("utf-8")            
            print(msg_rx)

            #Si se recibe el mensaje de sesion cerrada se cierra la conexion del cliente
    
        #Excecion en caso ocurran errores externos, no se cerrara conexion solo se mostrara el error
        except Exception as e:
            print(f"Exception: {e}")
        