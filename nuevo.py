# hay ciertos conceptos del POO que no se utilizan y podrian mejorar el programa
# como polimorfismo o delegacion (no se delega a clases inferiores el calcular precio)
# ademas el codigo esta muy acoplado, para agregar la clase premium deberia agregar un if mas en precio
# self.cl es poco expresivo en la clase Pasaje o TuristaEst podria ser TuristaEstudiante

import datetime

class Pasaje:
    def __init__(self, cliente):
        self.cliente = cliente
        #self.precio = self.cliente.calcular_precio()
        self.precio = cliente.base

        if self.is_invierno():
            self.precio *= 0.1

    def is_invierno(self):
        if datetime.date.today().month in [7,8]:
            return True
        elif datetime.date.today().month == 6 and datetime.date.today().day > 20:
            return True
        elif datetime.date.today().month == 9 and datetime.date.today().day < 20:
            return True
        else:
            return False


class Cliente:
    def __init__(self, clases):
        self.base = 500.0
        #self.clase = clase

        for clase in clases:
            self.base = clase.calcular_precio(self.base)


class Turista:
    def __init__(self):
        self.base = 500.0

    def calcular_precio(self):
        return self.base


class Estudiante:
    def __init__(self):
        self.descuento = 0.7

    def calcular_precio(self, base):
        return base * self.descuento


class Business:
    def __init__(self):
        self.recargo = 1.5

    def calcular_precio(self, base):
        return base * self.recargo


class Premium(Business):
    def __init__(self):
        super().__init__()
        self.propina = 200.0

    def calcular_precio(self, base):
        return super().calcular_precio(base) + self.propina


un_pasaje = Pasaje(Cliente([Estudiante(), Premium()]))
print(un_pasaje.precio)