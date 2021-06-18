from dataclasses import dataclass
import numpy as np
from pprint import pprint
from typing import List, Tuple, Any


@dataclass
class Poli:
    vertices: Any = None  # List[List[float]] = List
    arestas: Any = None
    origem: Tuple[float] = None  # (0.0, 0.0, 0.0)

    def __post_init__(self):
        """Do something after instancing"""
        self.vertices_para_arestas()

    def drawn(self):
        # to-do
        pass

    def vertices_para_arestas(self):
        """Should be implemented on children"""
        pass


class Cubo(Poli):
    @staticmethod
    def from_arestas(x: float = 1, y: float = 1, z: float = 1):
        return Cubo(
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
