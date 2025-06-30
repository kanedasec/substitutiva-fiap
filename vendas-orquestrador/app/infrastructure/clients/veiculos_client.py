import requests

class VeiculosClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def reservar(self, veiculo_id):
        try:
            resp = requests.patch(
                f"{self.base_url}/veiculos/{veiculo_id}/reserva",
                json={"reservado": True},
                timeout=5  # 5 segundos timeout
            )
            return resp.status_code == 200
        except Exception as e:
            print(f"[CLIENT VEICULOS] Erro ao reservar veículo {veiculo_id}: {e}")
            return False

    def desreservar(self, veiculo_id):
        if not veiculo_id or veiculo_id == "False":
            print("[CLIENT VEICULOS] ID inválido para desreservar:", veiculo_id)
            return False
        try:
            resp = requests.patch(
                f"{self.base_url}/veiculos/{veiculo_id}/reserva",
                json={"reservado": False},
                timeout=5  # limite de 5 segundos
            )
            return resp.status_code == 200
        except Exception as e:
            print(f"[CLIENT VEICULOS] Erro ao desreservar veículo {veiculo_id}: {e}")
            return False

    def baixar(self, veiculo_id):
        def baixar(self, veiculo_id):
            try:
                resp = requests.patch(
                    f"{self.base_url}/veiculos/{veiculo_id}/reserva",
                    json={"vendido": True},
                    timeout=5
                )
                return resp.status_code == 200
            except Exception as e:
                print(f"[CLIENT VEICULOS] Erro ao baixar veículo {veiculo_id}: {e}")
                return False
