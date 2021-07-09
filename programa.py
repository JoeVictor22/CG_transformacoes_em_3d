import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from objetos import Poligono, Retangulo, Piramide, TroncoPiramide
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


def centro_de_volume_dos_objetos(*poligonos: Poligono) -> np.array:
    """
    Calcula o ponto médio do centro de volume de varios objetos
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

    centro_do_volume = np.array(
        [[sum_x / qtd_centros, sum_y / qtd_centros, sum_z / qtd_centros]]
    )

    return centro_do_volume


def desenha_3d(
    ax,
    color,
    poli: Poligono,
    limite_max: float = 1.0,
    titulo: str = "Desenho",
    printar_origem: bool = True,
):
    """
    Chama o metodo para calcular faces e arestas e desenha um poligno tridimensional em um plot
    """

    # calcular arestas/faces
    poli.calcular_estruturas()

    # desenha todas as linhas do objeto
    for linha in poli.arestas:
        ax.plot(
            [linha[0][0], linha[1][0]],
            [linha[0][1], linha[1][1]],
            zs=[linha[0][2], linha[1][2]],
        )

    # desenha todas as faces do objeto
    ax.add_collection3d(
        Poly3DCollection(
            poli.faces,
            facecolors=color[0],
            linewidths=1.5,
            edgecolors=color[0],
            alpha=color[1],
        )
    )

    # caso deseje plotar os pontos de origem do objeto
    if printar_origem:
        ax.scatter(*poli.origem, c=color[0], marker="^")

    # define titulo e label para o plot
    ax.set_title(titulo)
    ax.set_xlabel("Eixo Y")
    ax.set_ylabel("Eixo X")
    ax.set_zlabel("Eixo Z")

    # define limites dos octantes para o plot
    ax.set_zlim3d(-limite_max, limite_max)
    ax.set_xlim3d(-limite_max, limite_max)
    ax.set_ylim3d(-limite_max, limite_max)

    # desenha o divisor de octantes
    ax.plot(
        [limite_max + 0.2, -limite_max - 0.2], [0, 0], [0, 0], color="Black", alpha=0.4
    )
    ax.plot(
        [0, 0], [limite_max + 0.2, -limite_max - 0.2], [0, 0], color="Black", alpha=0.4
    )
    ax.plot(
        [0, 0], [0, 0], [limite_max + 0.2, -limite_max - 0.2], color="Black", alpha=0.4
    )


def desenha_2d(color, poli: Poligono):
    """
    Desenha um poligono bidimensional
    """
    # calcular arestas/faces
    poli.calcular_estruturas()

    # para cada face, printa suas linhas
    for linha in poli.faces:
        coordenadas_em_2d = np.vstack((linha, linha[0]))
        x, y = zip(*coordenadas_em_2d)
        plt.plot(x, y, color)

    # desenha labels
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")


def cria_objetos() -> (Retangulo, Retangulo, Piramide, TroncoPiramide):
    """
    Cria os objetos com os parametros iniciais para todas as questões
    """
    # cubo : 1,5
    cubo = Retangulo.from_arestas(x=1.5, y=1.5, z=1.5)
    cubo.origem = (1.5 / 2, 1.5 / 2, 0)
    cubo.translacao((0, 0, 0))

    # paralelepipedo : 1.5, 5, 2.5
    paralelepipedo = Retangulo.from_arestas(x=1.5, y=5, z=2.5)
    paralelepipedo.origem = (0, 5 / 2, 0)
    paralelepipedo.translacao((0, 0, 0))

    # piramide : b=2 a=3, com rotacao de 45º
    piramide = Piramide.from_arestas(2, 2, 3)
    piramide.origem = (1, 1, 0)
    piramide.translacao((0, 0, 0))
    piramide.rotacao(45, "z")

    # # tronco : b=3 1.3 a=2.5
    tronco = TroncoPiramide.from_arestas(
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

    """
    Para cada objeto, cria um subplot e desenha o objeto
    """
    ax = fig.add_subplot(2, 2, 1, projection="3d")
    desenha_3d(ax=ax, poli=cubo, color=("blue", 0.1), limite_max=2, titulo="Cubo")

    ax = fig.add_subplot(2, 2, 2, projection="3d")
    desenha_3d(
        ax=ax,
        poli=paralelepipedo,
        color=("red", 0.1),
        limite_max=5.5,
        titulo="Paralelepipedo",
    )

    ax = fig.add_subplot(2, 2, 3, projection="3d")
    desenha_3d(
        ax=ax, poli=piramide, color=("orange", 0.1), limite_max=3.5, titulo="Pirâmide"
    )

    ax = fig.add_subplot(2, 2, 4, projection="3d")
    desenha_3d(
        ax=ax, poli=tronco, color=("green", 0.1), limite_max=3.5, titulo="Tronco"
    )

    plt.show()


def segunda_questao():
    """
    Segunda questão: Realiza operações de translação e desenha todos os objetos no mesmo sistema sem sobreposição
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 2, 1, projection="3d")

    cubo, paralelepipedo, piramide, tronco = cria_objetos()

    # Desenha no subplot os objetos originais
    desenha_3d(ax=ax, poli=cubo, color=("blue", 0.1))
    desenha_3d(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    desenha_3d(ax=ax, poli=piramide, color=("orange", 0.1))
    desenha_3d(
        ax=ax,
        poli=tronco,
        color=("green", 0.1),
        limite_max=6,
        titulo="Sólidos originais",
    )

    """
    Realiza as translações para cada octante
    """
    # primeiro octante
    cubo.translacao((1.5, 1.5, 0))
    piramide.translacao((3.5, 3.5, 0))

    # segundo octante
    paralelepipedo.translacao((-2, -3, 0))
    tronco.translacao((-4, -3, 3))

    ax = fig.add_subplot(1, 2, 2, projection="3d")
    ax.scatter(0, 0, 0, c="black")

    # Desenha em um subplot os objetos translados
    desenha_3d(ax=ax, poli=cubo, color=("blue", 0.1))
    desenha_3d(ax=ax, poli=paralelepipedo, color=("red", 0.1))
    desenha_3d(ax=ax, poli=piramide, color=("orange", 0.1))
    desenha_3d(
        ax=ax,
        poli=tronco,
        color=("green", 0.1),
        limite_max=6,
        titulo="Sólidos translados",
    )

    plt.show()


def terceira_questao(deve_plotar: bool = True) -> (Retangulo, Piramide):
    """
    Passa os objetos do sistema de coordenadas do mundo para o da câmera
    """
    # caso deseje plotar os objetos modificados
    ax = None
    if deve_plotar:
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection="3d")

    # objetos para questao
    cubo, _, piramide, _ = cria_objetos()

    # origem do olho/camera
    olho = (-2, 2, 2)

    # realizando translações da questao anterior
    cubo.translacao((1.5, 1.5, 0))
    piramide.translacao((3.5, 3.5, 0))

    # calcula os componentes para a matriz de rotacao
    ponto_medio_dos_octantes = centro_de_volume_dos_objetos(cubo, piramide)
    comp_n = np.subtract(ponto_medio_dos_octantes, olho)
    aux = (-2, 2, 4)
    comp_u = np.cross(comp_n, aux)  # produto vetorial do comp_u com aux
    comp_v = np.cross(comp_u, comp_n)  # produto vetorial do comp_u com aux

    # normalizando componentes
    comp_u = (comp_u / np.linalg.norm(comp_u))[0]
    comp_v = (comp_v / np.linalg.norm(comp_v))[0]
    comp_n = (comp_n / np.linalg.norm(comp_n))[0]

    # matriz de translação
    translacao_olho = np.array(
        [[1, 0, 0, -olho[0]], [0, 1, 0, -olho[1]], [0, 0, 1, -olho[2]], [0, 0, 0, 1]]
    )

    # matriz de rotação
    matriz_resultante = np.array(
        [
            [comp_u[0], comp_u[1], comp_u[2], 0],
            [comp_v[0], comp_v[1], comp_v[2], 0],
            [comp_n[0], comp_n[1], comp_n[2], 0],
            [0, 0, 0, 1],
        ]
    )

    """
    passando para o sistema da camera
    """
    # cria matriz v com as duas operações a serem realizadas
    v = np.dot(matriz_resultante, translacao_olho)
    # realiza as operações nos objetos
    cubo.vertices = translacao_de_matrizes(cubo.vertices, v)
    piramide.vertices = translacao_de_matrizes(piramide.vertices, v)

    # caso deseje plotar os objetos
    if deve_plotar:
        # desenhando objetos
        desenha_3d(ax=ax, poli=cubo, color=("red", 0.1), printar_origem=False)
        desenha_3d(
            ax=ax,
            poli=piramide,
            color=("green", 0.1),
            limite_max=6,
            titulo="Cenário Questão 3",
            printar_origem=False,
        )

        plt.show()
    else:
        # retorna os objetos modificados para a proxima questao
        return cubo, piramide


def quarta_questao():
    """
    Desenha os objetos do sistema de coordenadas da camera em 2D
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")

    # recebe os objetos no sistema da camera da questao anterior
    cubo, piramide = terceira_questao(deve_plotar=False)

    # vetor de transformação para 2d
    p = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    # transformações
    cubo.vertices = translacao_de_matrizes(cubo.vertices, p)
    piramide.vertices = translacao_de_matrizes(piramide.vertices, p)

    # desenha os objetos em 3d para comparação
    desenha_3d(ax=ax, poli=cubo, color=("red", 0.1), printar_origem=False)
    desenha_3d(
        ax=ax,
        poli=piramide,
        color=("green", 0.1),
        limite_max=6,
        titulo="Cenário Questão 4",
        printar_origem=False,
    )
    plt.show()

    plt.figure(figsize=(8, 8), dpi=80)

    # remove eixo Z dos objetos
    cubo.vertices = np.delete(cubo.vertices, 2, axis=1)
    piramide.vertices = np.delete(piramide.vertices, 2, axis=1)

    # desenha os objetos em 2d
    desenha_2d(poli=cubo, color="green")
    desenha_2d(poli=piramide, color="red")
    plt.show()


if __name__ == "__main__":
    primeira_questao()
    segunda_questao()
    terceira_questao()
    quarta_questao()
