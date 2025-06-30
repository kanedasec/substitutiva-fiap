from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.application.servico_pagamento import ServicoPagamento

router = APIRouter()
servico = ServicoPagamento()

class PagamentoInput(BaseModel):
    venda_id: str
    comprador_id: str
    veiculo_id: str

@router.post("/pagamentos")
def gerar_pagamento(input: PagamentoInput):
    pagamento = servico.gerar_pagamento(input.venda_id, input.comprador_id, input.veiculo_id)
    return pagamento

@router.get("/pagamentos/{codigo}")
def verificar_pagamento(codigo: str):
    pagamento = servico.verificar(codigo)
    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return {"codigo": codigo, "status": pagamento.status}

@router.post("/pagamentos/{codigo}/confirmar")
def confirmar_pagamento(codigo: str):
    sucesso = servico.confirmar_pagamento(codigo)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return {"codigo": codigo, "status": "pago"}
