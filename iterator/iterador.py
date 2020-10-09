
class iterator():
    def __init__(self, data):
        self.agregado = data
        self.conteo = 0

    def has_next(self):
        if self.conteo <= 1999:
            dato = self.agregado[self.conteo]
            self.conteo = self.conteo + 1
            return dato            
        else:
            return None
        