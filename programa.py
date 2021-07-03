import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poli, Cubo, Piramide, PiramideTronco
from pprint import pprint
from copy import copy


def draw_poli(ax, color, poli: Poli):

    poli.calcular_estruturas() # calcular arestas/faces

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

    ax.scatter(0,0,1, c="red")
    ax.scatter(0, 1, 0, c="green")
    ax.scatter(1, 0, 0, c="blue")

    ax.scatter(*poli.origem, c=color[0])


def plot(ax):

    ax.set_zlim3d(-6, 6)
    ax.set_xlim3d(-6, 6)
    ax.set_ylim3d(-6, 6)

    ax.set_title("Cenário 1")
    ax.set_xlabel("Eixo Y")
    ax.set_ylabel("Eixo X")
    ax.set_zlabel("Eixo Z")

    ax.plot([1.2, -1.2], [0, 0], [0, 0], color="Black", alpha=0.4)
    ax.plot([0, 0], [1.2, -1.2], [0, 0], color="Black", alpha=0.4)
    ax.plot([0, 0], [0, 0], [1.2, -1.2], color="Black", alpha=0.4)

    # plt.axis('off')
    # plt.grid(b=None)
    plt.show()

# def camera(camera_pos: tuple=(0,0,0), fuga_pos: tuple=(0,0,0)):
#
cubo = paralelepipedo = piramide = tronco = None

def primeira_questao():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 2, 1, projection="3d")

    # cubo : 1,5
    cubo = Cubo.from_arestas(x=1.5, y=1.5, z=1.5)
    cubo.origem = (1.5/2, 1.5/2, 0)
    cubo.translacao((0,0,0))
    draw_poli(ax=ax, poli=cubo, color=("blue", 0.1))

    ax = fig.add_subplot(1, 2, 2,projection='3d')
    # paralelepipedo : 1.5, 5, 2.5
    paralelepipedo = Cubo.from_arestas(x=1.5, y=5, z=2.5)
    paralelepipedo.origem = (0,5/2,0)
    paralelepipedo.translacao((0,0,0))
    draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1))

    plot(ax)

    # piramide : b=2 a=3
    # piramide = Piramide.from_arestas(2, 2, 3)
    # piramide.origem = (1,1, 0)
    # piramide.translacao((0,0,0))
    # piramide.rotacao(45, "z")
    #
    # # tronco : b=3 1.3 a=2.5
    # tronco = PiramideTronco.from_arestas(x_base=3, y_base=3, z=2.5, x_superior=1.3, y_superior=1.3)
    # tronco.origem = (3/2,3/2,0)
    # tronco.translacao((0,0,0))



    # def segunda_questao():
    #     # octante 1
    #     cubo.translacao((1.5, 1.5, 0))
    #     piramide.translacao((3.5 , 3.5, 0))
    #
    #     # octante 2
    #     paralelepipedo.translacao((-2, -3, 0))
    #     tronco.translacao((-4, -3, 0))
    #
    #
    # segunda_questao()
    # draw_poli(ax=ax, poli=cubo, color=("blue", 0.1))
    # draw_poli(ax=ax, poli=piramide, color=("gray", 0.1))
    # draw_poli(ax=ax, poli=tronco, color=("green", 0.1))
    # plot()

if __name__ == "__main__":
    primeira_questao()
    # segunda_questao()
    # main()

