from dataclasses import dataclass
import numpy as np
from pprint import pprint
from typing import List, Tuple, Any


@dataclass
class Poli:
    vertices: Any = None  # List[List[float]] = List
    arestas: Any = None
    origem: List[float] = None  # (0.0, 0.0, 0.0)
    _origem: Tuple[float] = None  # (0.0, 0.0, 0.0)
    x_y_z : Tuple[float] = None

    def __post_init__(self):
        """Do something after instancing"""
        self.vertices_para_arestas()

    def drawn(self):
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
        origem = [destino[index] - self.origem[index] for index, value in enumerate(destino)]
        for linha in self.vertices:
            for i in range(0,3):
                linha[i] += origem[i]

        self.origem = destino

        print(self.vertices)


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

        cubo.x_y_z = (x, y, z)

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
                self.vertices[4],
                self.vertices[7],
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
                    [0, 0, z],  # E
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
