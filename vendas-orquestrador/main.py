from fastapi import FastAPI
from app.adapters.input.fastapi_controller import router, criar_rotas
from app.infrastructure.clients.veiculos_client import VeiculosClient
from app.infrastructure.clients.compradores_client import CompradoresClient
from app.infrastructure.clients.pagamentos_client import PagamentosClient
from app.application.orquestrador_venda import OrquestradorVenda

app = FastAPI()

veiculos = VeiculosClient("http://veiculos-service:8000")
compradores = CompradoresClient("http://compradores-service:8001")
pagamentos = PagamentosClient("http://pagamentos-service:8003")

orquestrador = OrquestradorVenda(
    veiculos=veiculos,
    compradores=compradores,
    pagamentos=pagamentos
)

print("[MAIN] Criando rotas do orquestrador")
criar_rotas(orquestrador)

print("[MAIN] Incluindo router no FastAPI")
app.include_router(router)
