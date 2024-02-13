#Criar o ambiente virtual
mkvirtualenv famp-secao06 -p python3.10

#install libs
pip install fastapi psycopg2-binary sqlalchemy asyncpg sqlmodel uvicorn python-jose[cryptography] pytz passlib python-multipart pydantic_settings autopep8 pydantic[email]

#freeze 
pip freeze > requirements.txt

#desativar o ambiente virutal
deactivate

#ativar ambiente do python
source ~/.virtualenvs/famp-secao06/bin/activate

#live reload
uvicorn main:app --reload

#Balanceamento de carga
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker