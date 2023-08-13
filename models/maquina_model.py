from db import _executar
from departamento_model import Departamento
from companhia_model import Companhia
from Hardware.hardware_model import Hardware
from software_model import Software
from seguranca_model import Seguranca


class Maquina:

    teste = 'teste de __str__'
    __doc__ = 'Classe responsável pelo objeto MÁQUINA, onde ' \
              'será instanciado o obj de máquina.'

    def __init__(self, ip, nome, responsavel, funcao, setor=None, uid=None, nome_dep=None):
        super(Departamento).__init__(nome_dep)
        """
        :param ip: IP da máquina
        :param nome: Nome da máquina
        :param responsavel: Nome do responsável da máquina
        :param funcao: Função a qual aquela máquina pertence dentro do setor
        :param setor: Setor a qual a máquina se encontra
        """
        self.uid = uid
        self.__ip = ip
        self.__nome = nome
        self.__responsavel = responsavel
        self.__funcao = funcao
        self.__setor = setor
        print('Máquina criada com sucesso!')

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

    @staticmethod
    def buscar():
        return _executar(f'SELECT * FROM maquina;')

    @staticmethod
    def buscar_uid(uid):
        query = f'SELECT * FROM maquina WHERE id={int(uid)}'
        maquina = _executar(query)[0]
        maquina = Maquina(uid=maquina[0], ip=maquina[1], nome=maquina[2], responsavel=maquina[3],
                          funcao=maquina[4], setor=maquina[5])
        return maquina


