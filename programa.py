import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poli, Cubo, Piramide
from pprint import pprint


def draw_poli(ax, color, poli: Poli):
    for linha in poli.arestas:
        print(linha)
        ax.plot(
            [linha[0][0], linha[1][0]],
            [linha[0][1], linha[1][1]],
            zs=[linha[0][2], linha[1][2]],
        )

    ax.add_collection3d(Poly3DCollection(poli.faces, facecolors=color[0], linewidths=1.5, edgecolors=color[0], alpha=color[1]))


def main():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    cubo = Cubo.from_arestas(x=1, y=1, z=1)
    cubo.origem = (0,0,0)
    cubo.translacao(destino=(2,2,2))

    draw_poli(ax=ax, poli=cubo, color=("purple", 0.1))

    cubo.translacao(destino=(0,0,0))

    draw_poli(ax=ax, poli=cubo, color=("cyan", 0.1))


    ax.set_title("Cenário 1")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")
    plt.show()


if __name__ == "__main__":
    main()
