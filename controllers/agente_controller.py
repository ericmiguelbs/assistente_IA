from services.agente_service import AgenteService
from flask import request, jsonify
from models.db import db
from models.chatMensagem import chatMensagem

class agenteController:

    @staticmethod
    def registrar():
        data = request.get_json()
        pergunta_texto = data.get("pergunta")
        
        session_id = data.get("session_id", "sessao_padrao_123") 

        msg_usuario = chatMensagem(session_id=session_id, papel="user", interacao=pergunta_texto)
        db.session.add(msg_usuario)
        db.session.commit()

        historico_db = chatMensagem.query.filter_by(session_id=session_id)\
                                     .order_by(chatMensagem.id.desc())\
                                     .limit(6).all()
        historico_db.reverse()

        messages = []
        
        for msg in historico_db:
            messages.append({
                "role": msg.papel, 
                "content": msg.interacao
                })

        agent = AgenteService()
        resposta_texto = agent.agente(messages)

        msg_ia = chatMensagem(session_id=session_id, papel="assistant", interacao=resposta_texto)
        db.session.add(msg_ia)
        db.session.commit()

        return jsonify({
            "session_id": session_id,
            "pergunta": pergunta_texto,
            "resposta": resposta_texto
        })

    @staticmethod
    def historico():
        session_id = request.args.get("session_id")

        if session_id:
            mensagens = chatMensagem.query.filter_by(session_id=session_id).order_by(chatMensagem.id.asc()).all()
        else:
            mensagens = chatMensagem.query.order_by(chatMensagem.id.asc()).all()

        return jsonify([
            {
                "session_id": m.session_id,
                "papel": m.papel,
                "interacao": m.interacao,
                "data": m.data_criacao.isoformat()
            }
            for m in mensagens
        ])