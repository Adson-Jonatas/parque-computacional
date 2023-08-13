class Processador:

    __doc__ = 'Classe responsável pelo objeto PROCESSADOR, onde ' \
              'será instanciado o obj de processador.'

    def __init__(self, fabricante, tecnologia, gen):
        self.__fabricante = fabricante
        self.__tecnologia = tecnologia
        self.__gen = gen

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, novo):
        self.__fabricante = novo

    @property
    def tecnologia(self):
        return self.__tecnologia

    @tecnologia.setter
    def tecnologia(self, novo):
        self.__tecnologia = novo

    @property
    def gen(self):
        return self.__gen

    @gen.setter
    def gen(self, novo):
        self.__gen = novo