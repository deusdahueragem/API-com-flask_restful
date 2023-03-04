from flask import Flask
from flask_restful import Api
from tarefas import Todas_Tarefas, Listar_Tarefas

app = Flask(__name__)
api = Api(app)

api.add_resource(Todas_Tarefas, '/dev')
api.add_resource(Listar_Tarefas, '/dev/<int:id>')

if __name__ == '__main__':
    app.run(port=80, debug=True)