from app import app, db

class TblUsuario(db.Model): #tbl_usuario
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128), nullable = False)
    telefone = db.Column(db.String(15), nullable = False)
    senha = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return "Criando um usuario"
