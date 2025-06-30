# app/domain/veiculo.py

import uuid
from dataclasses import dataclass

@dataclass
class Veiculo:
    id: str
    marca: str
    modelo: str
    ano: int
    cor: str
    preco: float
    vendido: bool = False
    reservado: bool = False

    @staticmethod
    def criar(marca: str, modelo: str, ano: int, cor: str, preco: float) -> 'Veiculo':
        return Veiculo(
            id=str(uuid.uuid4()),
            marca=marca,
            modelo=modelo,
            ano=ano,
            cor=cor,
            preco=preco,
        )
