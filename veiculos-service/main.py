# main.py

from fastapi import FastAPI
from app.adapters.input.fastapi_controller import router, criar_rotas
from app.adapters.output.repositorio_em_memoria import RepositorioVeiculoEmMemoria

app = FastAPI()
repositorio = RepositorioVeiculoEmMemoria()

criar_rotas(repositorio)
app.include_router(router)