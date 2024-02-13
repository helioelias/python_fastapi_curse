"""Module providing a function printing python version."""

from typing import Dict, List, Optional,Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Query
from fastapi import Header
from fastapi import Depends

from time import sleep

from models import Curso
from models import Cursos

def fabe_db():
    try:
        print('Abrinco conexão com o bd..')
        sleep(1)
    finally:
        print('Fechando conexão com db')
        sleep(1)

app = FastAPI(
    title='API de Cursos',
    version='0.0.1',
    description='Uma api para estudo do FastAPI'
    )

@app.get('/cursos', 
         description='Retorna uma lista de cursos',
         summary='Retorna todos os cursos',
         response_model=List[Curso],
         response_description='Cursos encontrados com sucesso.')
async def get_cursos(db: Any = Depends(fabe_db)):
    return Cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id:int = Path(title='ID do curso', description='Dever ser entre 1 e 2', gt=0, lt=3), db: Any = Depends(fabe_db)):
    try:
        curso = Cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fabe_db)):
    next_id: int = len(Cursos) + 1
    curso.id = next_id
    Cursos.append(curso)
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fabe_db)):
    if curso_id in Cursos:
        Cursos[curso_id] = curso
        del curso.id       
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com ID {curso_id}')

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fabe_db)):
    if curso_id in cursos:
        del Cursos[curso_id]
        #return JSONResponse(content="Curso removido", status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com ID {curso_id}')

@app.get('/calculadora')
async def calcular(a:int = Query(default=None, gt=5), b:int= Query(default=None, gt=10), x_geek: str = Header(default=None), c:Optional[int]=None):
    soma:int = a + b
    if c:
        soma = soma + c
    
    print(f'X-GEEK: {x_geek}')
    
    return {"resultado": soma}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)
