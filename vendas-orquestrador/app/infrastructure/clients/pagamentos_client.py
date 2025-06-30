import requests

class PagamentosClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def gerar_codigo(self, venda_id, veiculo_id, comprador_id):
        try:
            resp = requests.post(
                f"{self.base_url}/pagamentos",
                json={
                    "venda_id": venda_id,
                    "comprador_id": comprador_id,
                    "veiculo_id": veiculo_id
                }
            )
            if resp.status_code == 200:
                return resp.json()["codigo"]
        except Exception as e:
            print("Erro ao gerar código de pagamento:", e)
        return None

    def verificar_pagamento(self, codigo):
        try:
            resp = requests.get(f"{self.base_url}/pagamentos/{codigo}")
            if resp.status_code == 200:
                return resp.json()["status"] == "pago"
        except Exception as e:
            print("Erro ao verificar pagamento:", e)
        return False
