from app import app, db

class TblCadastro(db.Model): #tbl_cadastro
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    senha = db.Column(db.String(128), nullable=False)


    def __repr__(self):
        return "Criando o cadastro de usuário."