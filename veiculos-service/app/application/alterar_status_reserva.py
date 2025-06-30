# app/application/alterar_status_reserva.py

class AlterarStatusReservaUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def executar(self, veiculo_id, reservado: bool):
        veiculo = self.repositorio.buscar_por_id(veiculo_id)
        if not veiculo:
            raise ValueError("Veículo não encontrado")

        veiculo.reservado = reservado
        self.repositorio.atualizar(veiculo)
        return veiculo
