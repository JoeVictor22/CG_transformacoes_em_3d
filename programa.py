import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poli, Cubo, Piramide
from pprint import pprint


def draw_poli(ax, color, poli: Poli):
    # ax.scatter3D(poli.arestas[:, 0], poli.arestas[:, 1], poli.arestas[:, 2])

    #   verts = [
    #         [Z[0],Z[1],Z[2],Z[3]],
    #         [Z[4],Z[5],Z[6],Z[7]],
    #         [Z[0],Z[1],Z[5],Z[4]],
    #         [Z[2],Z[3],Z[7],Z[6]],
    #         [Z[1],Z[2],Z[6],Z[5]],
    #         [Z[4],Z[7],Z[3],Z[0]]
    #       ]

    # for i in range(poli.arestas,2):
    #
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for linha in poli.arestas:
        print(linha)
        ax.plot(
            [linha[0][0], linha[1][0]],
            [linha[0][1], linha[1][1]],
            zs=[linha[0][2], linha[1][2]],
        )


    # verts = poli.vertices
    #
    # ax.add_collection3d(Poly3DCollection(verts, facecolors='b', linewidths=1.5, edgecolors='g'))


def main():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    cubo = Cubo.from_arestas(x=1, y=1, z=1)
    cubo.origem = (0,0,0)
    cubo.translacao(destino=(2,2,2))

    draw_poli(ax=ax, poli=cubo, color=("black", 0.1))

    cubo.translacao(destino=(0,0,0))

    draw_poli(ax=ax, poli=cubo, color=("black", 0.1))



    ax.set_title("Cenário 1")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")
    plt.show()


if __name__ == "__main__":
    # teste()
    # cubo = Cubo.from_arestas(x=1.5, y=1.5, z=1.5)
    #
    # main()
    #
    # piramide = Piramide.from_arestas(2, 2, 3)
    # teste2(piramide)

    main()
