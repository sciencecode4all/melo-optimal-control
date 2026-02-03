import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def plot_image(ax, entite) :
    demi_taille = entite.taille / 2  # définir une taille en unités d'axe
    ax.imshow(
        entite.image,
        extent=[
            entite.x[0] - demi_taille, entite.x[0] + demi_taille,
            entite.x[1] - demi_taille, entite.x[1] + demi_taille
        ],
        zorder=5
    )

def visualiser_simulation(env, chemin_sauvegarde, fps=25) : 

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
    for entite in env.entites : 
        if entite in env.obstacles : 
            # Afficher un cercle si entite est un obstacle
            circle = plt.Circle((entite.x[0], entite.x[1]),entite.r, color='gray', alpha=0.4, label=entite.nom)
            ax.add_patch(circle)
        else : 
            ax.plot(entite.x[0], entite.x[1], "ro" if entite.nom != "" else "", markersize=15, label=entite.nom if entite.nom != "" else "")
        # Afficher l'image
        plot_image(ax, entite)

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
    ani.save(chemin_sauvegarde, writer=PillowWriter(fps=fps))
