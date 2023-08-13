class Departamento:

    __doc__ = 'Classe responsável pelo objeto DEPARTAMENTO, onde ' \
              'será instanciado o obj de departamento.'

    def __init__(self, nome_dep):
        self.__nome_dep = nome_dep

    @property
    def nome_dep(self):
        return self.__nome_dep

    @nome_dep.setter
    def nome_dep(self, novo):
        self.__nome_dep = novo




