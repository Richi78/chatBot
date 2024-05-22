import pickle

class Peronsa:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def print_info(self):
        print(self.nombre)
        print(self.edad)
    
    def get_older(self, anios):
        self.edad += anios

# p1 = Peronsa('Mike', 25)
# p1.print_info()
# p1.get_older(6)

# with open('mike.pickle', 'wb') as f:
#     pickle.dump(p1, f)

with open('mike.pickle', 'rb') as f:
    p1 = pickle.load(f)

p1.print_info()