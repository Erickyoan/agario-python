from .iterador import iterator

class agregate():
    def __init__(self, data):
        self.data = data

    def get_iterador(self):
        return iterator(self.data)