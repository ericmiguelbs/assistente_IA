from models.db import db

class Perguntas(db.Model):
    __tablename__='perguntas'
    id = db.Column(db.Integer, primary_key = True)
    pergunta = db.Column(db.String(500), nullable = False)
    
