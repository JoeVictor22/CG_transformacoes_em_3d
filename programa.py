import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poli, Cubo, Piramide, PiramideTronco
from pprint import pprint


def draw_poli(ax, color, poli: Poli):
    for linha in poli.arestas:
        print(linha)
        ax.plot(
            [linha[0][0], linha[1][0]],
            [linha[0][1], linha[1][1]],
            zs=[linha[0][2], linha[1][2]],
        )

    ax.add_collection3d(
        Poly3DCollection(
            poli.faces,
            facecolors=color[0],
            linewidths=1.5,
            edgecolors=color[0],
            alpha=color[1],
        )
    )


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")


def plot():

    ax.set_zlim3d(-1, 1)
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)

    ax.set_title("Cenário 1")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")

    ax.plot([1.2, -1.2], [0, 0], [0, 0], color="Black", alpha=0.4)
    ax.plot([0, 0], [1.2, -1.2], [0, 0], color="Black", alpha=0.4)
    ax.plot([0, 0], [0, 0], [1.2, -1.2], color="Black", alpha=0.4)

    # plt.axis('off')
    # plt.grid(b=None)
    plt.show()


def main():

    # cubo : 1,5
    cubo = Cubo.from_arestas(x=1.5, y=1.5, z=1.5)
    cubo.origem = (0, 0, 0)
    # cubo.translacao(destino=(2,2,2))
    cubo.rotacao(angulo=50, eixo="x")
    cubo.rotacao(angulo=50, eixo="z")
    cubo.rotacao(angulo=50, eixo="y")
    draw_poli(ax=ax, poli=cubo, color=("purple", 0.1))

    #   # paralelepipedo : 1.5, 5, 2.5
    #   paralelepipedo = Cubo.from_arestas(x=1.5, y=5, z=2.5)
    #   paralelepipedo.origem = (0,0,0)
    #   draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    #
    #   # piramide : b=2 a=3
    #   piramide = Piramide.from_arestas(2, 3, 2)
    #   piramide.origem = (0,0,0)
    # #  piramide.translacao((4,4,4))
    #   draw_poli(ax=ax, poli=piramide, color=("gray", 0.1))
    #
    #   # tronco : b=3 1.3 a=2.5
    #   tronco = PiramideTronco.from_arestas(x_base=3, y_base=3, z=2.5, x_superior=1.3, y_superior=1.3)
    #   tronco.origem = (0,0,0)
    #  # tronco.translacao((-1,-1,-1))
    #   draw_poli(ax=ax, poli=tronco, color=("green", 0.1))

    plot()


if __name__ == "__main__":
    main()
