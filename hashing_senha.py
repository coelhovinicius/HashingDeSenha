import hashlib

def gerar_hash(senha):
    # Convertemos a string para bytes
    senha_bytes = senha.encode('utf-8')
    
    # Criamos o hash usando SHA-256
    hash_obj = hashlib.sha256(senha_bytes)
    
    # Retornamos o hash no formato hexadecimal
    return hash_obj.hexdigest()

# Exemplo de uso
senha = "minhaSenha123"
hash_resultado = gerar_hash(senha)

print(f"Senha original: {senha}")
print(f"Hash gerado: {hash_resultado}")

   