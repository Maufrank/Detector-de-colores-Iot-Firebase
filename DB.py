from firebase import firebase
# import request
# from flask import Blueprint, jsonify, render_template, request, json, redirect, session, send_file

from datetime import datetime


# base = firebase.FirebaseApplication("https://iot-firebase-11286-default-rtdb.firebaseio.com/", None)


class basedatos():
    base = ""
    
    def __init__(self):
        self.base = firebase.FirebaseApplication("https://iot-firebase-11286-default-rtdb.firebaseio.com/", None)
        

    def insertar_registro(self, rojo, verde, azul, color):
        id = 1
        res = self.base.get('/detector/registros', '')
        for res in res:
            id += 1
        hoy = datetime.now()
        fecha = hoy.date()
        hoy = datetime.now()
        hora = hoy.strftime("%H-%M-%S")
        datos = {
            "idRegistro": id,
            "rojo": rojo,
            "verde": verde,
            "azul": azul,
            "color": color,
            "fecha": fecha,
            "hora": hora
        }

        resultado = self.base.put('/detector/registros', f"{fecha}:{hora}", datos)

    def consultar(self):
        res = self.base.get('/detector/registros', '')
        resultado = "idRe\tcolor\tfecha\t\thora\n"
        data = ""
        for id in res:
            registro = res[id]
            data = f"{registro['idRegistro']}\t{registro['color']}\t{registro['fecha']}\t{registro['hora']}\n" + data
            
            # print(registro['azul'])
        resultado += data
        return resultado
    

# insertar_registro(12, 12, 12, "rojo")
# print(consultar())