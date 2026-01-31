# =========================
# Melo : le système mobile
# =========================

from gekko import GEKKO
import matplotlib.image as mpimg

class Melo:
    def __init__(self, m, x0, image:str, taille:float):
        """
        m, 
        x0, état initiale/actuelle de Mélo,
            position et vitesse
        image:str, image de Mélo pour l'affichage (png)
        taille:float, taille de Mélo pour l'affichage
        """
        self.m = GEKKO(remote=False)
        # États
        self.x  = m.Var(value=x0[0])
        self.y  = m.Var(value=x0[1])
        self.vx = m.Var(value=x0[2])
        self.vy = m.Var(value=x0[3])
        # Contrôles
        self.ax = m.MV(value=0)
        self.ay = m.MV(value=0)
        self.ax.STATUS = 1
        self.ay.STATUS = 1
        # Dynamique
        m.Equation(self.x.dt()  == self.vx)
        m.Equation(self.y.dt()  == self.vy)
        m.Equation(self.vx.dt() == self.ax)
        m.Equation(self.vy.dt() == self.ay)

        # Pour l'affichage
        self.image = mpimg.imread(image)
        self.taille = taille

    def cost(self, pomme_x, pomme_y):
        # minimiser la distance entre la pomme et mélo
        distance = (self.x - pomme_x)**2 + (self.y - pomme_y)**2
        # minimiser la vitesse de Mélo
        vitesse = self.vx**2 + self.vy**2
        # minimiser la commande (effort) de Mélo
        effort = self.ax**2 + self.ay**2
        return distance + vitesse + effort
    
    def mise_a_jour_etat(self, x_mesure) : 
        """
        Mise à jour de l'état actuel de Mélo 
        Entrée : 
        - x_mesure : nouvelles position et vitesse de Mélo
        """
        # position
        self.x  = self.m.Var(value=x_mesure[0])
        self.y  = self.m.Var(value=x_mesure[1])
        # vitesse
        self.vx = self.m.Var(value=x_mesure[2])
        self.vy = self.m.Var(value=x_mesure[3])