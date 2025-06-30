import uuid
from dataclasses import dataclass

@dataclass
class Pagamento:
    codigo: str
    status: str  # "pendente" ou "pago"
    venda_id: str
    comprador_id: str
    veiculo_id: str

    @staticmethod
    def criar(venda_id, comprador_id, veiculo_id):
        return Pagamento(
            codigo=str(uuid.uuid4())[:8],
            status="pendente",
            venda_id=venda_id,
            comprador_id=comprador_id,
            veiculo_id=veiculo_id
        )
