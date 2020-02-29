import random

class Movie:
    """Definimos la clase movie que contiene titulo y rango de atributos
    y tres metodos """
    def __init__(self, title):
        self.rank = random.randint(0,10)
        self.title = title.lower()
        print ("La pelicula \"" + self.title + "\" ha sido creada con  " + str(self.rank) + " de rank.")
    """
    Agregamos el atributo title y rank, este ultimo es un número random entre 0 y 10
    """
    def get_title(self):
        return(str(self.title))

    def get_rank(self):
        return(str(self.rank))

    def like(self):
        """ Aumenta en uno el rank"""
        self.rank += 1
        print("Ahora tiene "+str(self.rank)+ " de rank.")

    def dislike(self):
        """ Aumenta en uno el rank"""
        self.rank -= 1
        print("Ahora tiene "+str(self.rank)+ " de rank.")

    def lista(self):
        """ Imprime las iniciales del título de la pelicula en mayúsculas"""
        print("Nombre : %s\tRango: %d" % (self.title(), self.rank))

"""
creamos los metodos like y dislike que aumentan y disminuyen respectivamente una posición en el rank
"""
m1 = Movie("Parasites")
m1 = Movie("Minios")
m2 = Movie("Spiderman")
m3 = Movie("Spirit")
m4 = Movie("The Flash")
m5 = Movie("The Joker")
m6 = Movie("Terminator")
m7 = Movie("Cenicienta")
m8 = Movie("Buscando a Nemo")
m9 = Movie("Avengers")
m10 = Movie("Ant-man")
movies = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]


