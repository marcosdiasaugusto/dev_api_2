from flask import Flask
from flask_restful import Resource, Api, request
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0, 'nome': 'Marcos',
     'habilidades':['Python','Flask','Django']},
    {'id':1, 'nome': 'Denise',
     'habilidades':['Python','Django']},
    {'id': 2,
     "habilidades": [
            "História",
            "Geografia",
            "Relações Internacionais"
        ],
        "nome": "Henrique"
    },
    {
        "habilidades": [
            "Segurança do Trabalho",
            "Seguros",
            "Relações Internacionais"
        ],
        "id": 3,
        "nome": "Emily"
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        # return 'Ola dev'
        #return {'nome':'Marcos A. Dias'}
        try:
            # desenvolvedor = desenvolvedores[id]
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Contacte o administrador do API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído com Sucesso!'}
        return

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == "__main__":
    app.run(debug=True)
