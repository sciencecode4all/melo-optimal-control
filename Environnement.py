import numpy as np
from gekko import GEKKO
from Melo import Melo
# =========================
# Environnement
# =========================
class Environnement:
    def __init__(self,m, temps_total, N, Melo, pomme_objectif, obstacles=[], pommes=[]):
        self.m = m 
        self.m.time = np.linspace(0, temps_total, N)  # horizon
        # Système
        self.melo = Melo
        # Pomme (objectif)
        self.Pomme = pomme_objectif
        # Obstacles à éviter
        self.obstacles = obstacles
        # pour affichage
        self.pommes = pommes

    def setup_ocp(self):
        # Contrainte obstacle
        if self.obstacles : 
            for obstacle in self.obstacles : 
                self.m.Equation(obstacle.constrainte_cercle(self.melo))
        # Fonction objectif
        self.m.Obj(self.melo.cost(self.Pomme.x[0], self.Pomme.x[1]))
        # Mode contrôle optimal
        self.m.options.IMODE = 6

    def solve(self):
        self.m.solve(disp=False)

    def update_initial_state(self, x_mesure) : 
        self.melo.mise_a_jour_etat(x_mesure)

    def set_horizon(self, t0, t_end, N):
        self.m.time = np.linspace(t0, t_end, N)
