# app/application/editar_veiculo.py

class EditarVeiculoUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, veiculo_id, dados):
        veiculo = self.repositorio.buscar_por_id(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")

        veiculo.marca = dados.get("marca", veiculo.marca)
        veiculo.modelo = dados.get("modelo", veiculo.modelo)
        veiculo.ano = dados.get("ano", veiculo.ano)
        veiculo.cor = dados.get("cor", veiculo.cor)
        veiculo.preco = dados.get("preco", veiculo.preco)

        self.repositorio.atualizar(veiculo)
        return veiculo
