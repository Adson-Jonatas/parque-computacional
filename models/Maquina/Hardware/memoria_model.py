class Memoria:

    __doc__ = 'Classe responsável pelo objeto MEMÓRIA, onde ' \
              'será instanciado o obj de memória.'

    def __init__(self, tecnologia, capacidade):
        self.__tecnologia = tecnologia
        self.__capacidade = capacidade

    @property
    def tecnologia(self):
        return self.__tecnologia

    @tecnologia.setter
    def tecnologia(self, novo):
        self.__tecnologia = novo

    @property
    def capacidade(self):
        return self.__tecnologia

    @capacidade.setter
    def capacidade(self, novo):
        self.__capacidade = novo

