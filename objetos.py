from dataclasses import dataclass
import numpy as np
from typing import List, Tuple, Any
from math import sin, cos, radians
from copy import copy


@dataclass
class Poligono:
    """
    Classe pai para a implementação de diversos objetos
    """

    vertices: np.array = np.array([])
    arestas: np.array = np.array([])
    faces: np.array = np.array([])
    origem: Tuple = (0, 0, 0)

    def calcular_estruturas(self):
        """
        Monta as estruturas necessários para o plot do objeto
        """
        self.vertices_para_arestas()
        self.vertices_para_faces()

    def vertices_para_arestas(self):
        """Transforma os vertices do objeto em arestas"""
        pass

    def vertices_para_faces(self):
        """Transforma os vertices do objeto em faces"""
        pass

    def translacao(self, destino: Tuple):
        """
        Realiza a translação do objeto para uma posição (x,y,z)
        """
        origem = [
            destino[index] - self.origem[index] for index, value in enumerate(destino)
        ]
        matriz_de_translacao = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [origem[0], origem[1], origem[2], 1],
            ]
        )

        m_entrada = copy(self.vertices)
        m_entrada = np.hstack((m_entrada, np.ones((len(m_entrada), 1))))

        m_entrada = np.dot(m_entrada, matriz_de_translacao)

        self.vertices = np.delete(m_entrada, 3, axis=1)

        self.origem = destino

    def rotacao(self, angulo, eixo="x"):
        """
        Rotaciona o poligono de acordo com angulo e eixo
        """
        angulo = radians(angulo)
        if eixo == "x":
            rot_x = np.array(
                [
                    [1, 0, 0],
                    [0, cos(angulo), -sin(angulo)],
                    [0, sin(angulo), cos(angulo)],
                ]
            )
            self.vertices = np.dot(self.vertices, rot_x)

        if eixo == "y":
            rot_y = np.array(
                [
                    [cos(angulo), 0, sin(angulo)],
                    [0, 1, 0],
                    [-sin(angulo), 0, cos(angulo)],
                ]
            )
            self.vertices = np.dot(self.vertices, rot_y)

        if eixo == "z":
            rot_z = np.array(
                [
                    [cos(angulo), -sin(angulo), 0],
                    [sin(angulo), cos(angulo), 0],
                    [0, 0, 1],
                ]
            )
            self.vertices = np.dot(self.vertices, rot_z)

    def centro_de_massa(self) -> list[float]:
        """
        Calcula o centro de massa do objeto
        """
        sum_x = sum_y = sum_z = 0
        for ponto in self.vertices:
            sum_x += ponto[0]
            sum_y += ponto[1]
            sum_z += ponto[2]

        qtd_pontos = len(self.vertices)

        centro_de_massa = [sum_x / qtd_pontos, sum_y / qtd_pontos, sum_z / qtd_pontos]

        return centro_de_massa


class TroncoPiramide(Poligono):
    @staticmethod
    def from_arestas(
        x_base: float = 1,
        y_base: float = 1,
        z: float = 1,
        x_superior: float = 1,
        y_superior: float = 1,
    ) -> np.array:
        cubo = Retangulo(
            vertices=np.array(
                [
                    [0, 0, 0],  # A
                    [x_base, 0, 0],  # B
                    [x_base, y_base, 0],  # C
                    [0, y_base, 0],  # D
                    [(x_base - x_superior) / 2, (y_base - y_superior) / 2, z],  # E
                    [
                        (x_base - x_superior) / 2 + x_superior,
                        (y_base - y_superior) / 2,
                        z,
                    ],  # F
                    [
                        (x_base - x_superior) / 2 + x_superior,
                        (y_base - y_superior) / 2 + y_superior,
                        z,
                    ],  # G
                    [
                        (x_base - x_superior) / 2,
                        (y_base - y_superior) / 2 + y_superior,
                        z,
                    ],  # H
                ]
            )
        )

        return cubo

    def vertices_para_arestas(self):
        self.arestas = [
            [self.vertices[0], self.vertices[1]],  # A - B
            [self.vertices[1], self.vertices[2]],  # B - C
            [self.vertices[2], self.vertices[3]],  # C - D
            [self.vertices[3], self.vertices[0]],  # D - A
            [self.vertices[4], self.vertices[5]],  # E - F
            [self.vertices[5], self.vertices[6]],  # F - G
            [self.vertices[6], self.vertices[7]],  # G - H
            [self.vertices[7], self.vertices[4]],  # H - E
            [self.vertices[0], self.vertices[4]],  # A - E
            [self.vertices[1], self.vertices[5]],  # B - F
            [self.vertices[2], self.vertices[6]],  # C - G
            [self.vertices[3], self.vertices[7]],  # D - H
        ]

    def vertices_para_faces(self):
        self.faces = [
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
            ],  # A-B-C-D
            [
                self.vertices[4],
                self.vertices[5],
                self.vertices[6],
                self.vertices[7],
            ],  # E-F-G-H
            [
                self.vertices[2],
                self.vertices[3],
                self.vertices[7],
                self.vertices[6],
            ],  # C-D-H-G
            [
                self.vertices[1],
                self.vertices[2],
                self.vertices[6],
                self.vertices[5],
            ],  # B-C-G-F
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[5],
                self.vertices[4],
            ],  # A-B-F-E
            [
                self.vertices[0],
                self.vertices[3],
                self.vertices[7],
                self.vertices[4],
            ],  # A-D-H-E
        ]


class Retangulo(Poligono):
    @staticmethod
    def from_arestas(x: float = 1, y: float = 1, z: float = 1) -> np.array:
        cubo = Retangulo(
            vertices=np.array(
                [
                    [0, 0, 0],  # A
                    [x, 0, 0],  # B
                    [x, y, 0],  # C
                    [0, y, 0],  # D
                    [0, 0, z],  # E
                    [x, 0, z],  # F
                    [x, y, z],  # G
                    [0, y, z],  # H
                ]
            )
        )

        return cubo

    def vertices_para_arestas(self):
        self.arestas = [
            [self.vertices[0], self.vertices[1]],  # A - B
            [self.vertices[1], self.vertices[2]],  # B - C
            [self.vertices[2], self.vertices[3]],  # C - D
            [self.vertices[3], self.vertices[0]],  # D - A
            [self.vertices[4], self.vertices[5]],  # E - F
            [self.vertices[5], self.vertices[6]],  # F - G
            [self.vertices[6], self.vertices[7]],  # G - H
            [self.vertices[7], self.vertices[4]],  # H - E
            [self.vertices[0], self.vertices[4]],  # A - E
            [self.vertices[1], self.vertices[5]],  # B - F
            [self.vertices[2], self.vertices[6]],  # C - G
            [self.vertices[3], self.vertices[7]],  # D - H
        ]

    def vertices_para_faces(self):
        self.faces = [
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
            ],  # A-B-C-D
            [
                self.vertices[4],
                self.vertices[5],
                self.vertices[6],
                self.vertices[7],
            ],  # E-F-G-H
            [
                self.vertices[2],
                self.vertices[3],
                self.vertices[7],
                self.vertices[6],
            ],  # C-D-H-G
            [
                self.vertices[1],
                self.vertices[2],
                self.vertices[6],
                self.vertices[5],
            ],  # B-C-G-F
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[5],
                self.vertices[4],
            ],  # A-B-F-E
            [
                self.vertices[0],
                self.vertices[3],
                self.vertices[7],
                self.vertices[4],
            ],  # A-D-H-E
        ]


class Piramide(Poligono):
    @staticmethod
    def from_arestas(x: float = 1, y: float = 1, z: float = 1) -> np.array:
        return Piramide(
            vertices=np.array(
                [
                    [0, 0, 0],  # A
                    [x, 0, 0],  # B
                    [x, y, 0],  # C
                    [0, y, 0],  # D
                    [x / 2, y / 2, z],  # E
                ]
            )
        )

    def vertices_para_arestas(self):
        self.arestas = [
            [self.vertices[0], self.vertices[1]],  # A - B
            [self.vertices[1], self.vertices[2]],  # B - C
            [self.vertices[2], self.vertices[3]],  # C - D
            [self.vertices[3], self.vertices[0]],  # D - A
            [self.vertices[0], self.vertices[4]],  # A - E
            [self.vertices[1], self.vertices[4]],  # B - E
            [self.vertices[2], self.vertices[4]],  # C - E
            [self.vertices[3], self.vertices[4]],  # D - E
        ]

    def vertices_para_faces(self):
        self.faces = [
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
            ],  # A-B-C-D(BASE)
            [self.vertices[0], self.vertices[1], self.vertices[4]],  # A-B-E
            [self.vertices[1], self.vertices[2], self.vertices[4]],  # B-C-E
            [self.vertices[2], self.vertices[3], self.vertices[4]],  # C-D-E
            [self.vertices[3], self.vertices[0], self.vertices[4]],  # D-A-E
        ]
