class Pasaje:
    def __init__(self, cliente):
        self.cl = cliente

    def precio(self):
        final = 0
        # uso innecesario de condicionales que se podría reemplazar por polimorfismo y atributos de clase
        if self.cl.turista():
            final = self.cl.base()
        if self.cl.business():
            final = self.cl.base() * 1.5
        if self.cl.estudiante():
            final = final * self.cl.desc()
        return final


class Cliente:
    def base(self):  # deberia ser un atributo precio
        return 500.0

    def desc(self):  # deberia ser un atributo descuento
        return 0.70

    def turista(self):  # turista, business, y estudiante deberian ser subclases
        return False

    def business(self):
        return False

    def estudiante(self):
        return False


class Turista(Cliente):
    def turista(self):
        return True
    
    def base(self):
        return super().base()
    
    def desc(self):
        return super().desc()


class TuristaEst(Cliente):
    def turista(self):
        return True

    def estudiante(self):
        return True

    def base(self):
        return super().base()

    def desc(self):
        return super().desc()


class Business(Cliente):
    def business(self):
        return True

    def base(self):
        return super().base()

    def desc(self):
        return super().desc()


class BusinessEst(Cliente):
    def business(self):
        return True

    def estudiante(self):
        return True

    def base(self):
        return super().base()

    def desc(self):
        return super().desc()

un_pasaje = Pasaje(TuristaEst())
print(un_pasaje.precio())