# app/adapters/output/repositorio_em_memoria.py

class RepositorioCompradorEmMemoria:
    def __init__(self):
        self.compradores = {}

    def salvar(self, comprador):
        self.compradores[comprador.id] = comprador

    def buscar_por_id(self, comprador_id):
        return self.compradores.get(comprador_id)
