from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Chave secreta: {key.decode()}")
