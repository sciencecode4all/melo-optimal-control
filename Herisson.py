from Melo import Melo
import matplotlib.image as mpimg
# =========================
# Hérisson : obstacle cercle
# =========================
class Herisson:
    def __init__(self, x, r:float, image, taille, label="Hérisson"):
        """
        Permet d'initialiser un hérisson. 
        Le hérisson est modélisé par un cercle de centre (x,y) et de rayon r
        
        x:float, coordonnées du centre du cercle
        r:float, rayon du cercle
        image :str, image de l'hérisson pour l'affichage (png)
        taille :float, taille de l'image
        label: str, nom de l'obstacle
        """
        self.x = x 
        self.r = r
        # Pour l'affichage
        self.image = mpimg.imread(image)
        self.taille = taille 
        self.label = label

    def constrainte_cercle(self, melo:Melo):
        """
        Modélisation d'un obstacle circulaire à éviter. 
        Mélo doit rester en dehors du cercle.
        Cette fonction permet de vérifier cela.

        Retourne : 
        - True (vrai) si la contrainte est bien respectée (Mélo n'est pas dans le cercle)
        - False (faux) sinon
        """
        # équation d'un cercle
        # (x-)
        return (melo.x - self.x[0])**2 + (melo.y - self.x[1])**2 >= self.r**2