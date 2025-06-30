# app/domain/comprador.py

import uuid
from dataclasses import dataclass
from app.infrastructure.crypto import criptografar, descriptografar


@dataclass
class Comprador:
    id: str
    nome_criptografado: str
    cpf_criptografado: str
    email_criptografado: str
    endereco_criptografado: str

    @staticmethod
    def criar(nome: str, cpf: str, email: str, endereco: str) -> 'Comprador':
        return Comprador(
            id=str(uuid.uuid4()),
            nome_criptografado=criptografar(nome),
            cpf_criptografado=criptografar(cpf),
            email_criptografado=criptografar(email),
            endereco_criptografado=criptografar(endereco),
        )

    def nome(self):
        return descriptografar(self.nome_criptografado)

    def cpf(self):
        return descriptografar(self.cpf_criptografado)

    def email(self):
        return descriptografar(self.email_criptografado)

    def endereco(self):
        return descriptografar(self.endereco_criptografado)
