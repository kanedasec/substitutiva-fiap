# app/infrastructure/crypto.py

from cryptography.fernet import Fernet

# Substitua por variável de ambiente em produção
FERNET_KEY = b'ykm85IYcqzuSBC5i5FFNVvvOB_JUBF_dpDMu9-qU3Wc='  # Ex: b'suachavegerada...'

fernet = Fernet(FERNET_KEY)

def criptografar(valor: str) -> str:
    return fernet.encrypt(valor.encode()).decode()

def descriptografar(valor_criptografado: str) -> str:
    return fernet.decrypt(valor_criptografado.encode()).decode()
