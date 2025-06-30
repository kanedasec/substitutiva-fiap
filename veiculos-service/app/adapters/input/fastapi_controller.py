# app/adapters/input/fastapi_controller.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.application.cadastrar_veiculo import CadastrarVeiculoUseCase
from app.application.editar_veiculo import EditarVeiculoUseCase
from app.application.alterar_status_reserva import AlterarStatusReservaUseCase

router = APIRouter()

class VeiculoInput(BaseModel):
    marca: str
    modelo: str
    ano: int
    cor: str
    preco: float

class EditarVeiculoInput(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = None
    cor: Optional[str] = None
    preco: Optional[float] = None

class StatusReservaInput(BaseModel):
    reservado: bool

def criar_rotas(repositorio):
    cadastrar_use_case = CadastrarVeiculoUseCase(repositorio)
    editar_use_case = EditarVeiculoUseCase(repositorio)
    status_use_case = AlterarStatusReservaUseCase(repositorio)

    @router.post("/veiculos")
    def cadastrar_veiculo(input: VeiculoInput):
        veiculo = cadastrar_use_case.executar(
            input.marca, input.modelo, input.ano, input.cor, input.preco
        )
        return veiculo

    @router.get("/veiculos")
    def listar_disponiveis():
        return repositorio.listar_disponiveis()

    @router.get("/veiculos/vendidos")
    def listar_vendidos():
        return repositorio.listar_vendidos()

    @router.put("/veiculos/{veiculo_id}")
    def editar_veiculo(veiculo_id: str, input: EditarVeiculoInput):
        try:
            veiculo = editar_use_case.executar(veiculo_id, input.dict(exclude_unset=True))
            return veiculo
        except ValueError:
            raise HTTPException(status_code=404, detail="Veículo não encontrado")

    @router.patch("/veiculos/{veiculo_id}/reserva")
    def alterar_status_reserva(veiculo_id: str, input: StatusReservaInput):
        try:
            veiculo = status_use_case.executar(veiculo_id, input.reservado)
            return veiculo
        except ValueError:
            raise HTTPException(status_code=404, detail="Veículo não encontrado")

    @router.patch("/veiculos/{veiculo_id}/venda")
    def marcar_como_vendido(veiculo_id: str):
        try:
            veiculo = repositorio.marcar_como_vendido(veiculo_id)
            return veiculo
        except ValueError:
            raise HTTPException(status_code=404, detail="Veículo não encontrado")