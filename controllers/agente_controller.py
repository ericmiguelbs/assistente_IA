from services.agente_service import AgenteService
from flask import request, jsonify
from models.db import db
from models.perguntas import Perguntas
from models.respostas import Resposta


class agenteController:

    @staticmethod
    def registrar():
        data = request.get_json()
        pergunta_texto = data.get("pergunta")

        agent = AgenteService()

        messages = [
            {"role": "user", "content": pergunta_texto}
        ]

        # salva pergunta
        pergunta = Perguntas(pergunta=pergunta_texto)
        db.session.add(pergunta)
        db.session.commit()

        # gera resposta
        resposta_texto = agent.agente(messages)

        # salva resposta ligada à pergunta
        resposta = Resposta(
            resposta=resposta_texto,
            pergunta_id=pergunta.id
        )

        db.session.add(resposta)
        db.session.commit()

        return jsonify({
            "pergunta": pergunta_texto,
            "resposta": resposta_texto
        })
    @staticmethod
    def historico():
        respostas = Resposta.query.all()

        return jsonify([
            {
                "pergunta": r.pergunta.pergunta,
                "resposta": r.resposta,
                "data": r.data_criacao.isoformat()
            }
            for r in respostas
        ])