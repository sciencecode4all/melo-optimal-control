import matplotlib.image as mpimg

class Entite :
    def __init__(self, nom, x, image, taille) : 
        self.nom = nom
        self.x = x
        self.image = mpimg.imread(image)
        self.taille = taille 
