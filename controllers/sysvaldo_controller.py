from models.maquina_model import Maquina
from tornado.web import RequestHandler


class Index(RequestHandler):

    def get(self):
        listar = Maquina.listar()
        self.render('index.html', listar=listar)


class Cadastrar(RequestHandler):

    def get(self):
        self.render('novo.html')

    def post(self):

        ip = self.get_argument('ip', None)
        nome = self.get_argument('nome', None)
        responsavel = self.get_argument('responsavel', None)
        funcao = self.get_argument('funcao', None)
        setor = self.get_argument('setor', None)

        maquina = Maquina(ip, nome, responsavel, funcao, setor)
        maquina.cadastrar()

        self.redirect('/')


class Deletar(RequestHandler):

    def get(self, uid):
        delete = Maquina.buscar_uid(uid)
        delete.deletar()

        self.redirect('/')
