"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
"""
from db import _executar


class Maquina:

    teste = 'teste de __str__'
    __doc__ = 'Classe responsável pelo objeto MÁQUINA, onde ' \
              'será instanciado o obj de máquina.'

    def __init__(self, ip, nome, responsavel, funcao, setor=None, uid=None):
        self.uid = uid
        self.__ip = ip
        self.__nome = nome
        self.__responsavel = responsavel
        self.__funcao = funcao
        self.__setor = setor

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, novo):
        self.__ip = novo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo):
        self.__nome = novo

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, novo):
        self.__responsavel = novo

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, novo):
        self.__funcao = novo

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, novo):
        self.__setor = novo

    def cadastrar(self):
        query = (f"INSERT INTO maquina (ip, nome, responsavel, funcao, setor) values "
                 f"('{self.ip}', '{self.nome}', '{self.responsavel}', '{self.funcao}', '{self.setor}');")
        _executar(query)

    def atualizar(self):
        query = (f"UPDATE maquina SET ip='{self.ip}', nome='{self.nome}', responsavel='{self.responsavel}',"
                 f"funcao='{self.funcao}', setor='{self.setor}' WHERE id={self.uid};")
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM maquina WHERE id={self.uid};"
        _executar(query)

    @staticmethod
    def listar():
        teste = _executar(f'SELECT * FROM maquina;')
        return teste

    @staticmethod
    def buscar_uid(uid):
        query = f'SELECT * FROM maquina WHERE id={int(uid)};'
        maquina = _executar(query)[0]
        maquina = Maquina(uid=maquina[0], ip=maquina[1], nome=maquina[2], responsavel=maquina[3],
                          funcao=maquina[4], setor=maquina[5])
        return maquina
