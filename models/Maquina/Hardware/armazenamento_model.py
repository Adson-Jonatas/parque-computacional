class Armazenamento:

    __doc__ = 'Classe responsável pelo objeto HARDWARE, onde ' \
              'será instanciado o obj de hardware.'

    def __init__(self, tipo, capacidade):
        self.__tipo = tipo
        self.__capacidade = capacidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo):
        self.__tipo = novo

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, novo):
        self.__capacidade = novo