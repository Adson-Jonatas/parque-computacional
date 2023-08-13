class Companhia:

    __doc__ = 'Classe responsável pelo objeto COMPANHIA, onde ' \
              'será instanciado o obj de companhia.'

    def __init__(self, nome):
        self.__nome = nome
        print('Companhia criada com sucesso! ')  # LEMBRAR DE COMENTAR ESSE PRINT!

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo):
        self.__nome = novo
