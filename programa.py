import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poli, Cubo, Piramide, PiramideTronco
from copy import copy

def translacao_de_matrizes(vertices, matriz):
    """
    Realiza translacao de matrizes 3x3 com 4x4
    """
    m_entrada = copy(vertices)
    m_entrada = np.hstack((m_entrada, np.ones((len(m_entrada), 1))))
    m_entrada = np.dot(m_entrada, matriz)
    m_entrada = np.delete(m_entrada, 3, axis=1)
    return m_entrada


def draw_poli(
    ax,
    color,
    poli: Poli,
    limite_max: int = 1,
    titulo: str = "Desenho",
    printar_origem: bool = True,
):
    """
    Desenha um poligno tridimensional
    """

    poli.calcular_estruturas()  # calcular arestas/faces

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

    if printar_origem:
        ax.scatter(*poli.origem, c=color[0], marker="^")

    ax.set_title(titulo)
    ax.set_xlabel("Eixo Y")
    ax.set_ylabel("Eixo X")
    ax.set_zlabel("Eixo Z")

    ax.set_zlim3d(-limite_max, limite_max)
    ax.set_xlim3d(-limite_max, limite_max)
    ax.set_ylim3d(-limite_max, limite_max)

    ax.plot(
        [limite_max + 0.2, -limite_max - 0.2], [0, 0], [0, 0], color="Black", alpha=0.4
    )
    ax.plot(
        [0, 0], [limite_max + 0.2, -limite_max - 0.2], [0, 0], color="Black", alpha=0.4
    )
    ax.plot(
        [0, 0], [0, 0], [limite_max + 0.2, -limite_max - 0.2], color="Black", alpha=0.4
    )


def draw_plane(color, poli: Poli):
    """
    Desenha um poligono bidimensional
    """
    poli.calcular_estruturas()  # calcular arestas/faces

    for linha in poli.faces:
        coordenadas_em_2d = np.vstack((linha, linha[0]))
        x, y = zip(*coordenadas_em_2d)
        plt.plot(x, y, color)

    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")


def cria_objetos() -> (Cubo, Cubo, Piramide, PiramideTronco):
    """
    Cria os objetos com os parametros iniciais para todas as questões
    """
    # cubo : 1,5
    cubo = Cubo.from_arestas(x=1.5, y=1.5, z=1.5)
    cubo.origem = (1.5 / 2, 1.5 / 2, 0)
    cubo.translacao((0, 0, 0))

    # paralelepipedo : 1.5, 5, 2.5
    paralelepipedo = Cubo.from_arestas(x=1.5, y=5, z=2.5)
    paralelepipedo.origem = (0, 5 / 2, 0)
    paralelepipedo.translacao((0, 0, 0))

    # piramide : b=2 a=3
    piramide = Piramide.from_arestas(2, 2, 3)
    piramide.origem = (1, 1, 0)
    piramide.translacao((0, 0, 0))
    piramide.rotacao(45, "z")

    # # tronco : b=3 1.3 a=2.5
    tronco = PiramideTronco.from_arestas(
        x_base=3, y_base=3, z=2.5, x_superior=1.3, y_superior=1.3
    )
    tronco.origem = (3 / 2, 3 / 2, 0)
    tronco.translacao((0, 0, 0))

    return cubo, paralelepipedo, piramide, tronco


def primeira_questao():
    """
    Primeira questão: plota cada objeto em um sistema tridimensionmal
    """
    fig = plt.figure(figsize=(10, 10))

    cubo, paralelepipedo, piramide, tronco = cria_objetos()

    ax = fig.add_subplot(2, 2, 1, projection="3d")
    draw_poli(ax=ax, poli=cubo, color=("blue", 0.1), limite_max=2, titulo="Cubo")
    ax = fig.add_subplot(2, 2, 2, projection="3d")
    draw_poli(
        ax=ax,
        poli=paralelepipedo,
        color=("red", 0.1),
        limite_max=5.5,
        titulo="Paralelepipedo",
    )
    ax = fig.add_subplot(2, 2, 3, projection="3d")
    draw_poli(
        ax=ax, poli=piramide, color=("orange", 0.1), limite_max=3.5, titulo="Piramide"
    )
    ax = fig.add_subplot(2, 2, 4, projection="3d")
    draw_poli(ax=ax, poli=tronco, color=("green", 0.1), limite_max=3.5, titulo="Tronco")
    plt.show()


def segunda_questao():
    """
    Segunda questão: Realiza operações de translação e desenha todos os objetos no mesmo sistema sem sobreposição
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 2, 1, projection="3d")

    cubo, paralelepipedo, piramide, tronco = cria_objetos()

    draw_poli(ax=ax, poli=cubo, color=("blue", 0.1))
    draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    draw_poli(ax=ax, poli=piramide, color=("orange", 0.1))
    draw_poli(
        ax=ax,
        poli=tronco,
        color=("green", 0.1),
        limite_max=6,
        titulo="Sólidos originais",
    )

    # octante 1
    cubo.translacao((1.5, 1.5, 0))
    piramide.translacao((3.5, 3.5, 0))

    # octante 2
    paralelepipedo.translacao((-2, -3, 0))
    tronco.translacao((-4, -3, 3))

    ax = fig.add_subplot(1, 2, 2, projection="3d")
    ax.scatter(0, 0, 0, c="black")

    draw_poli(ax=ax, poli=cubo, color=("blue", 0.1))
    draw_poli(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    draw_poli(ax=ax, poli=piramide, color=("orange", 0.1))
    draw_poli(
        ax=ax,
        poli=tronco,
        color=("green", 0.1),
        limite_max=6,
        titulo="Sólidos translados",
    )
    plt.show()


def centro_de_volume_dos_objetos(*poligonos: Poli) -> np.array:
    """
    Calcula o ponto médio do centro de volume dos objetos
    """
    sum_x = sum_y = sum_z = 0
    centros_de_massas = []
    for poli in poligonos:
        centros_de_massas.append(poli.centro_de_massa())

    for centro in centros_de_massas:
        sum_x += centro[0]
        sum_y += centro[1]
        sum_z += centro[2]

    qtd_centros = len(centros_de_massas)

    centro_do_volume = [[sum_x / qtd_centros, sum_y / qtd_centros, sum_z / qtd_centros]]

    return centro_do_volume


def terceira_questao(deve_plotar: bool = True) -> (Cubo, Piramide):
    """
    Passa os objetos do sistema de coordenadas do mundo para o da câmera
    """
    if deve_plotar:
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection="3d")

    # objetos para trabalho
    cubo, _, piramide, _ = cria_objetos()
    # origem do olho
    olho = (-2, 2, 2)

    # realizando transformacoes da questao anterior
    cubo.translacao((1.5, 1.5, 0))
    piramide.translacao((3.5, 3.5, 0))

    ponto_medio_dos_octantes = centro_de_volume_dos_objetos(cubo, piramide)
    comp_n = np.subtract(ponto_medio_dos_octantes, olho)
    aux = (-2, 2, 4)
    comp_u = np.cross(comp_n, aux)  # produto vetorial do comp_u com aux
    comp_v = np.cross(comp_u, comp_n)  # produto vetorial do comp_u com aux

    # normalizando componentes
    comp_u = (comp_u / np.linalg.norm(comp_u))[0]
    comp_v = (comp_v / np.linalg.norm(comp_v))[0]
    comp_n = (comp_n / np.linalg.norm(comp_n))[0]

    # vetor de translação
    translacao_olho = np.array(
        [[1, 0, 0, -olho[0]], [0, 1, 0, -olho[1]], [0, 0, 1, -olho[2]], [0, 0, 0, 1]]
    )

    # vetor de rotação
    matriz_resultante = np.array(
        [
            [comp_u[0], comp_u[1], comp_u[2], 0],
            [comp_v[0], comp_v[1], comp_v[2], 0],
            [comp_n[0], comp_n[1], comp_n[2], 0],
            [0, 0, 0, 1],
        ]
    )

    # passando para o sistema da camera
    v = np.dot(matriz_resultante, translacao_olho)
    cubo.vertices = translacao_de_matrizes(cubo.vertices, v)
    piramide.vertices = translacao_de_matrizes(piramide.vertices, v)

    if deve_plotar:
        # desenhando objetos
        draw_poli(ax=ax, poli=cubo, color=("red", 0.1), printar_origem=False)
        draw_poli(
            ax=ax,
            poli=piramide,
            color=("green", 0.1),
            limite_max=6,
            titulo="Cenário Questão 3",
            printar_origem=False,
        )

        plt.show()
    else:
        return cubo, piramide


def quarta_questao():
    """
    Desenha os objetos do sistema de coordenadas da camera em 2D
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    # recebe os objetos no sistema da camera
    cubo, piramide = terceira_questao(deve_plotar=False)

    # transformacao para 2d
    p = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    cubo.vertices = translacao_de_matrizes(cubo.vertices, p)
    piramide.vertices = translacao_de_matrizes(piramide.vertices, p)

    # desenha em 3d
    draw_poli(ax=ax, poli=cubo, color=("red", 0.1), printar_origem=False)
    draw_poli(
        ax=ax,
        poli=piramide,
        color=("green", 0.1),
        limite_max=6,
        titulo="Cenário Questão 4",
        printar_origem=False,
    )
    plt.show()

    plt.figure(figsize=(8, 8), dpi=80)

    # removendo eixo Z dos objetos
    cubo.vertices = np.delete(cubo.vertices, 2, axis=1)
    piramide.vertices = np.delete(piramide.vertices, 2, axis=1)

    # desenha em 2d
    draw_plane(poli=cubo, color="green")
    draw_plane(poli=piramide, color="red")
    plt.show()


if __name__ == "__main__":
    primeira_questao()
    segunda_questao()
    terceira_questao()
    quarta_questao()
