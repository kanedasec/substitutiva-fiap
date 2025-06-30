# app/adapters/input/fastapi_controller.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.application.cadastrar_comprador import CadastrarCompradorUseCase

router = APIRouter()

class CompradorInput(BaseModel):
    nome: str
    cpf: str
    email: str
    endereco: str

def criar_rotas(repositorio):
    use_case = CadastrarCompradorUseCase(repositorio)

    @router.post("/compradores")
    def cadastrar(input: CompradorInput):
        comprador = use_case.executar(input.nome, input.cpf, input.email, input.endereco)
        return comprador

    @router.get("/compradores/{comprador_id}")
    def buscar(comprador_id: str):
        comprador = repositorio.buscar_por_id(comprador_id)
        if not comprador:
            raise HTTPException(status_code=404, detail="Comprador não encontrado")

        return {
            "id": comprador.id,
            "nome": comprador.nome(),
            "cpf": comprador.cpf(),
            "email": comprador.email(),
            "endereco": comprador.endereco()
        }
