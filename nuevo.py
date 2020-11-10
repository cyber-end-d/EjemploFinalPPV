class Pasaje:
    def __init__(self, cliente):
        self.cliente = cliente

    def precio(self):
        return self.cliente.calcular_precio()


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