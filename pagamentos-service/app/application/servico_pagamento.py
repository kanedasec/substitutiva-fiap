from app.domain.pagamentos import Pagamento

class ServicoPagamento:
    def __init__(self):
        self.pagamentos = {}

    def gerar_pagamento(self, venda_id, comprador_id, veiculo_id):
        pagamento = Pagamento.criar(venda_id, comprador_id, veiculo_id)
        self.pagamentos[pagamento.codigo] = pagamento
        return pagamento

    def verificar(self, codigo):
        return self.pagamentos.get(codigo)

    def confirmar_pagamento(self, codigo):
        if codigo in self.pagamentos:
            self.pagamentos[codigo].status = "pago"
            return True
        return False
