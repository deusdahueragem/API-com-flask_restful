from flask_restful import Resource, request
import json

tarefas = [
    {'tarefa':'Limpar a Casa'},
    {'tarefa':'Codar'},
    {'tarefa':'Trocar a Lampada'},
    {'tarefa':'Responder Chats'}
]

class Todas_Tarefas(Resource):
    def get(self):
        return tarefas
    
    def post(self):
        try:
            dados = json.loads(request.data)
            tarefas.append(dados)
            lenposition = len(tarefas) - 1
            return tarefas[lenposition]
        except:
            return {'status':'erro', 'mensagem':'Houve um erro durante a insercao do registro'}
        
class Listar_Tarefas(Resource):
    def get(self, id):
        return tarefas[id]
    def delete(self, id):
        try:
            tarefas.pop(id)
            return {'status':'Sucesso', 'mensagem':'Tarefa deletada com sucesso'}
        except IndexError:
            return {'status':'Erro', 'mensagem':'ID inexistente'}
        except:
            return {'status':'Erro', 'mensagem':'Erro nao identificado'}
    def put(self, id):
        try:
            dados = json.loads(request.data)
            tarefas[id] = dados
            return {'status':'Sucesso', 'mensagem':'Dados alterados com sucesso'}
        except IndexError:
            return {'status':'Erro', 'mensagem':'ID inexistente'}
        except:
            return {'status':'Erro', 'mensagem':'Erro nao identificado'}