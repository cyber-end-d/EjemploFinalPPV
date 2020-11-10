import datetime

class Pasaje:
    def __init__(self, cliente):
        self.cliente = cliente

    def precio(self):
        if self.is_invierno():
            return self.cliente.calcular_precio() * 0.1
        else:
            return self.cliente.calcular_precio()

    def is_invierno(self):
        if datetime.date.today().month in [7,8]:
            return True
        if datetime.date.today().month == 6 and datetime.date.today().day > 20:
            return True
        if datetime.date.today().month == 9 and datetime.date.today().day < 20:
            return True
        else:
            return False

class Cliente:
    def __init__(self):
        self.precio = 500.0
        self.descuento = 0.7

    def calcular_precio(self):  # polimorfismo
        pass

class Turista(Cliente):
    def calcular_precio(self):
        return self.precio


class TuristaEst(Cliente):
    def calcular_precio(self):
        return self.precio * self.descuento


class Business(Cliente):
    def calcular_precio(self):
        return self.precio * 1.5


class BusinessEst(Cliente):
    def calcular_precio(self):
        return self.precio * 1.5 * self.descuento


class Premium(Cliente):
    def calcular_precio(self):
        return self.precio * 1.5 + 200

un_pasaje = Pasaje(TuristaEst())
print(un_pasaje.precio())