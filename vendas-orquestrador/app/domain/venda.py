from dataclasses import dataclass
import uuid

@dataclass
class Venda:
    id: str
    veiculo_id: str
    comprador_id: str
    status: str  # iniciado, reservado, pago, concluido, cancelado

    @staticmethod
    def iniciar(veiculo_id, comprador_id):
        return Venda(id=str(uuid.uuid4()), veiculo_id=veiculo_id, comprador_id=comprador_id, status="iniciado")
