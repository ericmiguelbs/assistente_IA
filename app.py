import os
from models.db import db
from flask import Flask
from config import Config
from controllers.agente_controller import agenteController


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule('/pergunta', view_func=agenteController.registrar, methods =['POST'],endpoint='pergunta')
app.add_url_rule('/historico', view_func=agenteController.historico, methods =['GET'],endpoint='historico')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)