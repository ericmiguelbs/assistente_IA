from models.db import db
from sqlalchemy import ForeignKey
from datetime import datetime

class Resposta(db.Model):
    __tablename__ = 'respostas'

    id = db.Column(db.Integer, primary_key=True)
    resposta = db.Column(db.Text, nullable=False)

    pergunta_id = db.Column(db.Integer, ForeignKey("perguntas.id"))

    pergunta = db.relationship("Perguntas")

    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)