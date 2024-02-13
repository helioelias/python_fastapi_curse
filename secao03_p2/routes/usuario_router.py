"""Module providing a function printing python version."""
from fastapi import APIRouter

router = APIRouter()


@router.get('/api/v1/usuarios')
async def get_usuarios():
    return {'info': 'Todos os usuários'}