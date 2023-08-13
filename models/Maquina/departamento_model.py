class Departamento:

    __doc__ = 'Classe responsável pelo objeto DEPARTAMENTO, onde ' \
              'será instanciado o obj de departamento.'

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo):
        self.__nome = novo




