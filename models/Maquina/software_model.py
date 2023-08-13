
class Software:

    __doc__ = 'Classe responsável pelo objeto SOFTWARE, onde ' \
              'será instanciado o obj de software.'

    def __init__(self, so, versao):
        self.__so = so
        self.__versao = versao
        print('Software criado com sucesso! ')  # LEMBRAR DE COMENTAR ESSE PRINT!

    @property
    def so(self):
        return self.__so

    @so.setter
    def so(self, novo):
        self.__so = novo

    @property
    def versao(self):
        return self.__versao

    @versao.setter
    def versao(self, novo):
        self.__versao = novo

