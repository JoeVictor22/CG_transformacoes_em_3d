from dataclasses import dataclass
import numpy as np
from pprint import pprint
from typing import List, Tuple, Any
from math import sin, cos, radians
from copy import copy


@dataclass
class Poli:
    vertices: Any = None  # List[List[float]] = List
    arestas: Any = None
    faces: Any = None
    origem: List[float] = (0, 0, 0)  # (0.0, 0.0, 0.0)
    _origem: Tuple[float] = (0, 0, 0)  # (0.0, 0.0, 0.0)

    def __post_init__(self):
        """Do something after instancing"""
        pass

    def calcular_estruturas(self):
        self.vertices_para_arestas()
        self.vertices_para_faces()

    def draw(self):
        # to-do
        pass

    def vertices_para_arestas(self):
        """Should be implemented on children"""

    def vertices_para_faces(self):
        """Should be implemented on children"""
        pass

    # def __setattr__(self, key, value):
    #     if key == "_origem": # expeting a tuple
    #         if not isinstance(value, Tuple):
    #             raise ValueError
    #
    #         self.origem = list(value)
    #         self._origem = value
    #     else:
    #         return super().__setattr__(key, value)

    def translacao(self, destino: Tuple):
        origem = [
            destino[index] - self.origem[index] for index, value in enumerate(destino)
        ]
        matriz_de_translacao = np.array(
            [
                [1,0,0, 0],
                [0,1,0, 0],
                [0,0,1, 0],
                [origem[0],origem[1],origem[2], 1]
            ]
        )


        m_entrada = copy(self.vertices)
        m_entrada = np.hstack((m_entrada, np.ones((len(m_entrada), 1))))

        m_entrada = np.dot(m_entrada, matriz_de_translacao)

        self.vertices = np.delete(m_entrada, 3, axis=1)

        self.origem = destino


    def rotacao(self, angulo, eixo="x"):
        angulo = radians(angulo)
        if eixo == "x":
            rot_x = np.array(
                [
                    [1, 0, 0],
                    [0, cos(angulo), -sin(angulo)],
                    [0, sin(angulo), cos(angulo)]
                ]
            )
            self.vertices = np.dot(self.vertices, rot_x)

        if eixo == "y":
            rot_y = np.array(
                [
                    [cos(angulo), 0, sin(angulo)],
                    [0, 1, 0],
                    [-sin(angulo), 0, cos(angulo)]
                ]
            )
            self.vertices = np.dot(self.vertices, rot_y)

        if eixo == "z":
            rot_z = np.array(
                [
                    [cos(angulo), -sin(angulo), 0],
                    [sin(angulo), cos(angulo), 0],
                    [0, 0, 1]
                ]
            )
            self.vertices = np.dot(self.vertices, rot_z)


class PiramideTronco(Poli):
    @staticmethod
    def from_arestas(
        x_base: float = 1,
        y_base: float = 1,
        z: float = 1,
        x_superior: float = 1,
        y_superior: float = 1,
    ):
        cubo = Cubo(
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


class Cubo(Poli):
    @staticmethod
    def from_arestas(x: float = 1, y: float = 1, z: float = 1):
        cubo = Cubo(
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


class Piramide(Poli):
    @staticmethod
    def from_arestas(x: float = 1, y: float = 1, z: float = 1):
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
        # A - B, A - C, A - D, A - E
        # B - E
        # C - E
        # D - E

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


if __name__ == "__main__":
    print("asd")
    cubo = Cubo.from_arestas(x=1.5, y=1.5, z=1.5)
    # cubo = cubo.origem( (0.5 ** (x*x + y*y)) * 0.5)

    paralelepipedo = Cubo.from_arestas(1.5, 5, 2.5)
    # paralelepipedo = paralelepipedo.origem((paralelepipedo.vertices[0][0]+paralelepipedo.vertices[3][0])/2,(paralelepipedo.vertices[0][1]+paralelepipedo.vertices[3][1])/2,(paralelepipedo.vertices[0][2]+paralelepipedo.vertices[3][2])/2)

    piramide = Piramide.from_arestas(2, 2, 3)

    pprint(cubo.arestas)
    pprint(paralelepipedo.arestas)
    pprint(piramide.arestas)
