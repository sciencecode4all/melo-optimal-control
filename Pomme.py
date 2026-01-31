import matplotlib.image as mpimg

class Pomme :
    def __init__(self, nom, x, image, taille) : 
        #TODO : optimiser avec héritage ... 
        self.nom = nom
        self.x = x
        self.image = mpimg.imread(image)
        self.taille = taille 
