import serial
import sys

class SerialChat:
    
    def transmitir(self, serial):
        dato_enviar = input("[Tu] ")
        print("")
        dato_enviar = dato_enviar + "\n"
        #Se envia el dato al otro terminal
        serial.write(dato_enviar.encode())
        #Se espera por confimacion de que se recibio 
        confirmacion = serial.readline()
        #Si se recibe confirmacion entonces se cambia el modo a receptor
        if (confirmacion.decode() == "OK\n"):
            self.transmisor = False

    def recibir(self, serial):
        dato_recibir = serial.readline()
        #Imprime en consola lo recibido
        print("[Usuario] " + dato_recibir.decode())
        #Envia la confirmacion de que se recibió el mensaje
        serial.write("OK\n".encode())
        #Cambia el modo a transmisor otra vez
        self.transmisor = True

def main():
    serial_chat = SerialChat()
    serial_chat.transmisor = False
    print("ChatOn 6.0")
    print("=============")
    puerto = input("Ingrese el puerto (/dev/ttyUSB1): ")
    #Y es tranmisor, n es receptor. El otro terminal debe configurarse al reves
    inicia_transmision = input("Comienza la transmision (Y/n)")
    if (inicia_transmision == "Y"):
        serial_chat.transmisor = True
    print("Sesion Actual\n")
    
    try:
        #Configuracion de puerto y apertura
        s = serial.Serial(puerto,9600)
        #Se limpia el buffer por si acaso hubiera data remanente
        s.flushInput()
        while (True):
            if(serial_chat.transmisor):
                serial_chat.transmitir(s)
            else:
                serial_chat.recibir(s)
        #Cierra el puerto
        s.close()
    except Exception as e: 
        print(e)

if __name__ == "__main__":
    main()