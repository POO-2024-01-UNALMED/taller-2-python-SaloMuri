class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self, asientos):
        numeroAsientos = 0
        i == 0
        for i in i < len(self.asientos):
            if (asientos[i] != ""):
                numeroAsientos += 1
                i += 1
        return numeroAsientos
    
    def verificarIntegridad(self, asientos, registro):
        i = 0
        if (self.registro == self.motor.registro):
            for i in i < len(self.asientos):
                if (asientos[i] != ""):
                    if (asientos[i].registro != registro):
                        respuesta = "Las piezas no son originales"
                    respuesta = "Auto original"
                else:
                    respuesta = "Las piezas no son originales"
        return respuesta


    
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if (tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo