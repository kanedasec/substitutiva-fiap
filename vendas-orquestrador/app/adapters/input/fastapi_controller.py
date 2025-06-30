from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.application.orquestrador_venda import OrquestradorVenda

router = APIRouter()

class VendaInput(BaseModel):
    veiculo_id: str
    comprador_id: str

def criar_rotas(orquestrador):
    @router.post("/vendas")
    def iniciar_venda(input: VendaInput):
        resultado = orquestrador.iniciar_venda(input.veiculo_id, input.comprador_id)
        return resultado

    @router.post("/vendas/{venda_id}/concluir")
    def concluir_venda(venda_id: str):
        resultado = orquestrador.concluir_venda(venda_id)
        if not resultado:
            raise HTTPException(status_code=404, detail="Venda não encontrada")
        return resultado
