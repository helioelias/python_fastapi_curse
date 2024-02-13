""" imports """
from passlib.context import CryptContext

CRYPTO = CryptContext(schemes=['bcrypt'])

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta
    comparando a senha em texto puro, informado pelo usuario
    e o hash da senha que estará salvo no banco de dados
    durante a criação da conta
    """
    return CRYPTO.verify(senha, hash_senha)
    
def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    return CRYPTO.hash(senha)