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

    def cantidadAsientos(self):
        asientosReales = 0
        i = 0
        cantidadVeces = len(self.asientos)
        for i  in i < cantidadVeces:
            if i != "":
                asientosReales += 1
            i += 1
        return asientosReales

        
    def verificarIntegridad(self):
        cantidadVeces = len(self.asientos)
        if self.registro == self.motor:
            for i in range(cantidadVeces):
                if self.asientos[i] != "":
                    if self.asientos[i] != self.registro:
                        return "Las piezas no son originales"
                else:
                    return "Auto original"
            else:
                return "Las piezas no son originales"



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