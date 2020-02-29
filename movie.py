import random

class Movies:
    """Definimos la clase movie que contiene titulo y rango de atributos
    y tres metodos """
    def __init__(self, title):
        self.rank = random.randint(0,10)
        self.title = title.lower()
        print ("La pelicula " + self.title + "esta en la posición " + str(self.rank) + " de rango")
    """
    Agregamos el atributo title y rank, este ultimo es un número random entre 0 y 10
    """
    def get_title(self)
    return(str(self.title))

    def get_rank(self)
    return(str(self.rank))

    def like(self):
        self.rank += 1
        print("Ahora esta en la posición "+str(self.rank))

    def dislike(self):
        self.rank -= 1
        print ("Ahora esta en la posición "+str(self.rank))
"""
creamos los metodos like y dislike que aumentan y disminuyen respectivamente una posición en el rank
"""


