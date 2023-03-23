from vista import miVentana, frame1, frame2, boton1, boton2, rojo, blanco, naranja, verde, azul, estado_color, back_color, registrosT, frame3, conx
from DB import basedatos
from controllerArduino import arduino
import threading
import time

estaCorriendo = True
modo = 'manual'

def ocultar():
    modo = True
    frame2.pack_forget()
    
    
    
def mostrar():
    frame3.pack_forget()
    
    frame2.pack(fill='both', expand=True)
    frame3.pack(fill='both', expand=True)
    
    # modo.set('n')
    modo = False
    

    
    
def decodificar(cadena, opcion):
    hola = cadena.split('|')
    if(opcion == 'rojo'):
        rojo = hola[0].split(':')
        return (rojo[1]).rstrip()
    elif(opcion == 'verde'):
        verde = hola[1].split(':')
        return (verde[1]).rstrip()
    elif(opcion == 'azul'):
        azul = hola[2].split(':')
        return (azul[1]).rstrip()
    elif(opcion == 'color'):
        color = hola[3].split(':')
        return (color[1]).rstrip()
    
def cambio_color(color):
    arduino.moverServo(color)
    # lect = arduino.puerto()
    # color_reg = decodificar(lect, "color")
    # db.insertar_registro(0, 0, 0, color)
    # estado_color.set(color)
    # consulta = db.consultar()
    # registrosT.set(consulta)
    # estado_color.set('hola')
    # if color_reg == 'rojo':
    #     print('esto es rojo')
        
    #     back_color.set('red')
    
def leerSensores():
    while True:
        try:

            lectura = arduino.puerto()
            if lectura:
                color = decodificar(lectura, "color")
                print(lectura)
                estado_color.set(color)
                # if modo == 'automatico':
                db.insertar_registro(decodificar(lectura, "rojo"),decodificar(lectura, "verde"), decodificar(lectura, "azul"), decodificar(lectura, "color"))
        except Exception:
            print('sin lectura')
            # while True:
            #     estado_color.set('E')
            #     time.sleep(0.5)
            #     estado_color.set('Er')
            #     time.sleep(0.5)
            #     estado_color.set('Err')
            #     time.sleep(0.5)
            #     estado_color.set('Erro')
            #     time.sleep(0.5)
            #     estado_color.set('Error')
            #     time.sleep(0.5)
                
            
            
            
            


def finalizar():
    estaCorriendo= False
    hiloSensor.join(0.1)
    tabla.join(0.1)
    miVentana.quit()
    miVentana.destroy()
    # arduino.close()
    
        
def datosTabla():
    while estaCorriendo:
        consulta = db.consultar()
        registrosT.set(consulta)
        time.sleep(4)
    
 


if __name__ == '__main__':
    modo = False
    
    miVentana.protocol("WM_DELETE_WINDOW", finalizar)
    hiloSensor = threading.Thread(target=leerSensores, daemon=True)
    
    tabla = threading.Thread(target=datosTabla, daemon=True)
    
    
    boton2.config(command=lambda:ocultar())
    boton1.config(command=lambda:mostrar())
    rojo.config(command=lambda:cambio_color('rojo'))
    blanco.config(command=lambda:cambio_color('blanco'))
    naranja.config(command=lambda:cambio_color('naranja'))
    verde.config(command=lambda:cambio_color('verde'))
    azul.config(command=lambda:cambio_color('azul'))
    
    db = basedatos()
    arduino = arduino('COM4')
    # hiloSensor.start()
    
    # tabla.start()
    
    # lect = arduino.consultar_servo()
    # print(lect)
    
    # lectura = arduino.consultar_servo()
    # # color = decodificar(lectura, "color")
    # print(lectura)
    # estado_color.set(lectura)
    
    # consulta = db.consultar()
    # registrosT.set(consulta)
    
    # datos = decodificar(arduino.consultar_servo(), "color")
    # print(datos)
    # # if datos:
    # #     back_color.set(datos)
        
    col = arduino.consultar_servo()
    
    if col:
        estado_color.set(col)
        # hiloSensor.start()
    
        # tabla.start()
    else:
        conx.set("ERROR al conectar con Arduino")
    try:
        time.sleep(1)
        hiloSensor.start()
    
        tabla.start()
    except Exception:
        print('Error al lanzar el hilo...')
        
    
    
    miVentana.mainloop()
# finalizar()