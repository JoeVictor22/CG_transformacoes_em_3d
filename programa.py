import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poli, Cubo, Piramide, PiramideTronco
from pprint import pprint
from copy import copy


def draw_poli(ax, color, poli: Poli, limite_max: int = 1, titulo: str="Desenho"):

    poli.calcular_estruturas() # calcular arestas/faces

    for linha in poli.arestas:
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

    # Marcadores dos eixos
    # ax.scatter(0,0,1, c="gray", marker='^')
    # ax.scatter(0, 1, 0, c="gray", marker='^')
    # ax.scatter(1, 0, 0, c="gray", marker='^')
    print(*poli.origem,poli.origem[0],poli.origem[1],poli.origem[2]+1)
    print(*poli.origem, poli.origem[0], poli.origem[1]+1, poli.origem[2])

    '''SOMENTE NA QUESTAO 1
    ax.text(*poli.origem, "Origem", c=color[0])

    ax.quiver(*poli.origem,1,0,0, color=color[0])
    ax.quiver(*poli.origem,0,1,0, color=color[0])
    ax.quiver(*poli.origem,0,0,1, color=color[0])
    '''

    ax.scatter(*poli.origem, c=color[0], marker='^')

    ax.set_title(titulo)
    ax.set_xlabel("Eixo Y")
    ax.set_ylabel("Eixo X")
    ax.set_zlabel("Eixo Z")

    ax.set_zlim3d(-limite_max, limite_max)
    ax.set_xlim3d(-limite_max, limite_max)
    ax.set_ylim3d(-limite_max, limite_max)

    ax.plot([limite_max + 0.2, -limite_max - 0.2], [0, 0], [0, 0], color="Black", alpha=0.4)
    ax.plot([0, 0], [limite_max + 0.2, -limite_max - 0.2], [0, 0], color="Black", alpha=0.4)
    ax.plot([0, 0], [0, 0], [limite_max + 0.2, -limite_max - 0.2], color="Black", alpha=0.4)


def plot(ax):
    #
    # ax.set_zlim3d(-6, 6)
    # ax.set_xlim3d(-6, 6)
    # ax.set_ylim3d(-6, 6)
    #
    # ax.set_title("Cenário 1")
    # ax.set_xlabel("Eixo Y")
    # ax.set_ylabel("Eixo X")
    # ax.set_zlabel("Eixo Z")
    #
    # ax.plot([1.2, -1.2], [0, 0], [0, 0], color="Black", alpha=0.4)
    # ax.plot([0, 0], [1.2, -1.2], [0, 0], color="Black", alpha=0.4)
    # ax.plot([0, 0], [0, 0], [1.2, -1.2], color="Black", alpha=0.4)

    # plt.axis('off')
    # plt.grid(b=None)
    plt.show()

# def camera(camera_pos: tuple=(0,0,0), fuga_pos: tuple=(0,0,0)):
#

def cria_objetos():

    # cubo : 1,5
    cubo = Cubo.from_arestas(x=1.5, y=1.5, z=1.5)
    cubo.origem = (1.5/2, 1.5/2, 0)
    cubo.translacao((0,0,0))

    # paralelepipedo : 1.5, 5, 2.5
    paralelepipedo = Cubo.from_arestas(x=1.5, y=5, z=2.5)
    paralelepipedo.origem = (0,5/2,0)
    paralelepipedo.translacao((0,0,0))

    # piramide : b=2 a=3
    piramide = Piramide.from_arestas(2, 2, 3)
    piramide.origem = (1,1, 0)
    piramide.translacao((0,0,0))
    piramide.rotacao(45, "z")

    # # tronco : b=3 1.3 a=2.5
    tronco = PiramideTronco.from_arestas(x_base=3, y_base=3, z=2.5, x_superior=1.3, y_superior=1.3)
    tronco.origem = (3/2,3/2,0)
    tronco.translacao((0,0,0))

    return cubo, paralelepipedo, piramide, tronco

def primeira_questao():
    fig = plt.figure(figsize=(10, 10))

    cubo, paralelepipedo, piramide, tronco = cria_objetos()

    ax = fig.add_subplot(2, 2, 1, projection="3d")
    draw_poli(ax=ax, poli=cubo, color=("blue", 0.1), limite_max=2, titulo="Cubo")
    ax = fig.add_subplot(2, 2, 2, projection='3d')
    draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1), limite_max=5.5, titulo="Paralelepipedo")
    ax = fig.add_subplot(2, 2, 3, projection='3d')
    draw_poli(ax=ax, poli=piramide, color=("orange", 0.1), limite_max=3.5, titulo="Piramide")
    ax = fig.add_subplot(2, 2, 4, projection='3d')
    draw_poli(ax=ax, poli=tronco, color=("green", 0.1), limite_max=3.5, titulo="Tronco")
    plot(ax)

def segunda_questao():
    fig = plt.figure(figsize=(10, 10))

    cubo, paralelepipedo, piramide, tronco = cria_objetos()

    # octante 1
    cubo.translacao((1.5, 1.5, 0))
    piramide.translacao((3.5 , 3.5, 0))

    # octante 2
    paralelepipedo.translacao((-2, -3, 0))
    tronco.translacao((-4, -3, 3))

    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(0,0,0, c="black")

    draw_poli(ax=ax, poli=cubo, color=("blue", 0.1))
    draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    draw_poli(ax=ax, poli=piramide, color=("orange", 0.1))
    draw_poli(ax=ax, poli=tronco, color=("green", 0.1), limite_max=6, titulo="Cenário Questão 2")
    plot(ax)

def terceira_questao():
    def centro_vol_visão(*poligonos: Poli):
        sum_x = sum_y = sum_z = 0
        centros_de_massas = []
        for poli in poligonos:
            centros_de_massas.append(poli.centro_de_massa())

        for centro in centros_de_massas:
            sum_x += centro[0]
            sum_y += centro[1]
            sum_z += centro[2]

        qtd_centros = len(centros_de_massas)

        centro_do_volume = [[sum_x/qtd_centros, sum_y/ qtd_centros, sum_z/qtd_centros]]

        return centro_do_volume

    fig = plt.figure(figsize=(10, 10))
    cubo, paralelepipedo, piramide, tronco = cria_objetos()

    # origem do system
    olho = (-2,2,2)
    ponto_medio_dos_octantes = centro_vol_visão(tronco, paralelepipedo)

    comp_u = np.subtract(ponto_medio_dos_octantes, olho)
    aux = (0.3,0.2,0.5) #lixo aleatorio
    comp_v = np.cross(comp_u, aux)      # produto vetorial do comp_u com aux
    comp_n = np.cross(comp_v, comp_u)   # produto vetorial do comp_u com aux

    # normalizar
    comp_u = (comp_u / np.linalg.norm(comp_u))[0]
    comp_v = (comp_v / np.linalg.norm(comp_v))[0]
    comp_n = (comp_n / np.linalg.norm(comp_n))[0]

    paralelepipedo.translacao((-olho[0], -olho[1], -olho[2]))
    tronco.translacao((-olho[0], -olho[1], -olho[2]))

    matriz_resultante = np.array(
        [
            [comp_u[0], comp_u[1], comp_u[2], 0],
            [comp_v[0], comp_v[1], comp_v[2], 0],
            [comp_n[0], comp_n[1], comp_n[2], 0],
            [0,0,0,1]
        ]
    )

    m_entrada = copy(paralelepipedo.vertices)
    m_entrada = np.hstack((m_entrada, np.ones((len(m_entrada), 1))))
    m_entrada = np.dot(m_entrada, matriz_resultante)
    paralelepipedo.vertices = np.delete(m_entrada, 3, axis=1)

    m_entrada = copy(tronco.vertices)
    m_entrada = np.hstack((m_entrada, np.ones((len(m_entrada), 1))))
    m_entrada = np.dot(m_entrada, matriz_resultante)
    tronco.vertices = np.delete(m_entrada, 3, axis=1)


    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(0,0,0, c="black")

    draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    draw_poli(ax=ax, poli=tronco, color=("green", 0.1), limite_max=6, titulo="Cenário Questão 2")
    plot(ax)


if __name__ == "__main__":
    # primeira_questao()
    # segunda_questao()
    terceira_questao()


