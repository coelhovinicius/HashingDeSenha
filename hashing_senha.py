''' Criação de Hash de senha '''

import hashlib


def gerar_hash(senha):
    ''' Convertemos a string para bytes '''
    senha_bytes = senha.encode('utf-8')

    # Criamos o hash usando SHA-256
    hash_obj = hashlib.sha256(senha_bytes)

    # Retornamos o hash no formato hexadecimal
    return hash_obj.hexdigest()


# Exemplo de uso
SENHA = "minhaSenha123"
HASH_RESULTADO = gerar_hash(SENHA)

print(f"Senha original: {SENHA}")
print(f"Hash gerado: {HASH_RESULTADO}")
