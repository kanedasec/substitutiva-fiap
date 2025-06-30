# app/application/cadastrar_veiculo.py

from app.domain.veiculo import Veiculo

class CadastrarVeiculoUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, marca, modelo, ano, cor, preco):
        veiculo = Veiculo.criar(marca, modelo, ano, cor, preco)
        self.repositorio.salvar(veiculo)
        return veiculo
