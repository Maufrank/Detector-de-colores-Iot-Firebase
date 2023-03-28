from firebase import firebase
from datetime import datetime




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
        hora = hoy.strftime("%H:%M:%S")
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
        resultado = []
        for id in res:
            registro = res[id]
            resultado.append([registro['idRegistro'], registro['color'], registro['fecha'], registro['hora']])
        return resultado
