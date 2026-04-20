from models.db import db
from datetime import datetime


class chatMensagem(db.Model):
    __tablename__='chatMensagem'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False, index=True)
    papel = db.Column(db.String(20), nullable=False)
    interacao = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Mensagem {self.session_id} - {self.role}'
    