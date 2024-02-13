#Criar o ambiente virtual
mkvirtualenv famp-secao04 -p python3.10

#install libs
pip install fastapi psycopg2-binary sqlalchemy asyncpg uvicorn

#freeze 
pip freeze > requirements.txt

#desativar o ambiente virutal
deactivate

#ativar ambiente do python
source ~/.virtualenvs/famp-secao04/bin/activate

#live reload
uvicorn main:app --reload

#Balanceamento de carga
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker