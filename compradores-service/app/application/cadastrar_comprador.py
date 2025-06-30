# app/application/cadastrar_comprador.py

from app.domain.comprador import Comprador

class CadastrarCompradorUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, nome, cpf, email, endereco):
        comprador = Comprador.criar(nome, cpf, email, endereco)
        self.repositorio.salvar(comprador)
        return comprador
