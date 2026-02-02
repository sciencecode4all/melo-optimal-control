import numpy as np
from Environnement import Environnement
from Melo import Melo
from Herisson import Herisson
from Pomme import Pomme
from affichage import visualiser_simulation
from gekko import GEKKO

m = GEKKO()

# Mélo
x0_melo = np.concatenate((np.array([1.5, 7]), np.zeros(2)))
image_melo = "src/melo.png"
taille_melo = 2.5
melo = Melo(m, x0_melo, image_melo, taille_melo)

# Pomme
x_pomme = np.array([4.5, 2.5]) 
image_pomme = "src/pomme.png"
taille_pomme = 1.25
pomme = Pomme("objectif", x_pomme, image_pomme, taille_pomme)

# Pommier (pour affichage)
x_pommier = np.array([5.8, 3.8]) 
image_pommier = "src/pommier.png"
taille_pommier = 4
pommier = Pomme("pommier", x_pommier, image_pommier, taille_pommier)

# Hérisson
x_herisson = np.array([3,4.5])
rayon_herisson = 1
image_herisson = "src/herisson.png"
taille_herisson = 2
herisson = Herisson(x_herisson, rayon_herisson, image_herisson, taille_herisson, label="Hérisson")

obstacles = [herisson]

temps_total = 5 #s
N = 100 #nombre de pas

env = Environnement(m, temps_total, N, melo, pomme, obstacles, [pommier])
env.setup_ocp()
env.solve()

# Résultats
print("Position finale de Melo :", env.melo.x.VALUE[-1], env.melo.y.VALUE[-1])
print("Vitesse finale de Melo  :", env.melo.vx.VALUE[-1], env.melo.vy.VALUE[-1])

visualiser_simulation(env)