# Faça o clone do Projeto

# Instale o venv
- py -m venv env

# Acesse o ambiente virtual
- ./venv/Scrypts/activate

# Instale as bibliotecas
- pip install -r requirements.txt

# Faça a Migração
- flask db init
- flask db migrate -m "Initial migration."
- flask db upgrade

# Execução do Projeto
- Flask run
