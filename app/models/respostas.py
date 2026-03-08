from models.db import db
from sqlalchemy import ForeignKey

class Resposta(db.Model):
    __tablename__ = 'respsotas'
    id = db.Column(db.Integer, primary_key = True)
    resposta = db.Column(db.String, nullable = False)

    id_pergunta = db.Column(db.Integer, ForeignKey("perguntas.id"))