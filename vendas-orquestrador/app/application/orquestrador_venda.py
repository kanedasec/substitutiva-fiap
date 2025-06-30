# app/application/orquestrador_venda.py

from app.domain.venda import Venda

class OrquestradorVenda:
    def __init__(self, veiculos, compradores, pagamentos):
        self.veiculos = veiculos
        self.compradores = compradores
        self.pagamentos = pagamentos
        self.vendas_em_memoria = {}  # apenas simulação, substitua por DB se necessário

    def iniciar_venda(self, veiculo_id, comprador_id):
        print("[ORQUESTRADOR] Iniciando venda")
        venda = Venda.iniciar(veiculo_id, comprador_id)
        print("[ORQUESTRADOR] Venda criada:", venda.id)

        print("[ORQUESTRADOR] Reservando veículo...")
        if not self.veiculos.reservar(veiculo_id):
            venda.status = "cancelado"
            return venda

        print("[ORQUESTRADOR] Verificando comprador...")
        if not self.compradores.verificar(comprador_id):
            print("[ORQUESTRADOR] Comprador inválido, desreservando...")
            self.veiculos.desreservar(veiculo_id)
            venda.status = "cancelado"
            return venda

        codigo_pagamento = self.pagamentos.gerar_codigo(venda.id, veiculo_id, comprador_id)
        if not codigo_pagamento:
            self.veiculos.desreservar(veiculo_id)
            venda.status = "cancelado"
            return venda


        venda.status = "aguardando_pagamento"
        self.vendas_em_memoria[venda.id] = (venda, codigo_pagamento)


        # ✅ Retorne também o código de pagamento
        return {
            "id": venda.id,
            "veiculo_id": venda.veiculo_id,
            "comprador_id": venda.comprador_id,
            "status": venda.status,
            "codigo_pagamento": codigo_pagamento
        }

    def concluir_venda(self, venda_id):
        dados = self.vendas_em_memoria.get(venda_id)
        if not dados:
            return None

        venda, codigo = dados

        if not self.pagamentos.verificar_pagamento(codigo):
            return venda  # ainda aguardando

        self.veiculos.baixar(venda.veiculo_id)
        venda.status = "concluido"
        return venda

