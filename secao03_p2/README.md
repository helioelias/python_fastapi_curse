#Criar o ambiente virtual
mkvirtualenv famp-secao02 -p python3.10

#desativar o ambiente virutal
deactivate

#ativar ambiente do python
source ~/.virtualenvs/famp-secao03/bin/activate

#instalar o fastapi
pip install fastapi uvicorn

#freeze
pip freeze > requirements.txt

#live reload
uvicorn main:app --reload

#Balanceamento de carga
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker