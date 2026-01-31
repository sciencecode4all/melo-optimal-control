import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def visualiser_simulation(env) : 

    # Récupération des trajectoires
    x = env.melo.x.VALUE
    y = env.melo.y.VALUE

    # Création de la figure
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 8)

    # Mélo
    traj_line, = ax.plot([], [], 'b--', alpha=0.5, label="Trajectoire de Mélo") #trajectoire
    demi = env.melo.taille / 2 
    # Charger l’image 
    melo_img = ax.imshow(
        env.melo.image,
        extent=[x[0]-demi, x[0]+demi, y[0]-demi, y[0]+demi],
        zorder=5
    )

    # Pomme (objectif)
    ax.plot(env.Pomme.x[0], env.Pomme.x[1], "ro", markersize=15, label='Pomme')
    demi_pomme = env.Pomme.taille / 2  # définir une taille en unités d'axe
    ax.imshow(
        env.Pomme.image,
        extent=[
            env.Pomme.x[0] - demi_pomme, env.Pomme.x[0] + demi_pomme,
            env.Pomme.x[1] - demi_pomme, env.Pomme.x[1] + demi_pomme
        ],
        zorder=5
    )

    # autres images 
    for element in env.pommes : 
        demi_taille = element.taille / 2  # définir une taille en unités d'axe
        ax.imshow(
            element.image,
            extent=[
                element.x[0] - demi_taille, element.x[0] + demi_taille,
                element.x[1] - demi_taille, element.x[1] + demi_taille
            ],
            zorder=5
        )
    

    # Hérisson (obstacle)
    for obs in env.obstacles:
        # ax.plot(obs.x[0], obs.x[1], 'gray', marker="o", markersize=15, label=obs.label)
        # Cercle (optionnel)
        circle = plt.Circle((obs.x[0], obs.x[1]), obs.r, color='gray', alpha=0.4, label=obs.label)
        ax.add_patch(circle)
        
        demi_obs = obs.taille / 2  # taille en unités d'axe
        ax.imshow(
            obs.image,
            extent=[
                obs.x[0] - demi_obs, obs.x[0] + demi_obs,
                obs.x[1] - demi_obs, obs.x[1] + demi_obs
            ],
            zorder=5
        )

    ax.legend()

    def update(frame):
        xm, ym = x[frame], y[frame]

        demi = env.melo.taille / 2
        melo_img.set_extent([
            xm - demi, xm + demi,
            ym - demi, ym + demi
        ])

        traj_line.set_data(x[:frame], y[:frame])
        return melo_img, traj_line


    ani = FuncAnimation(
        fig,
        update,
        frames=len(x),
        interval=40,
        blit=False
    )

    plt.show()
    ani.save("simulation.gif", writer=PillowWriter(fps=25))
