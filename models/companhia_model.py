class Companhia:

    __doc__ = 'Classe responsável pelo objeto COMPANHIA, onde ' \
              'será instanciado o obj de companhia.'

    def __init__(self, com_nome):
        self.__com_nome = com_nome
        print('Companhia criada com sucesso! ')  # LEMBRAR DE COMENTAR ESSE PRINT!

    @property
    def com_nome(self):
        return self.__com_nome

    @com_nome.setter
    def com_nome(self, novo):
        self.__com_nome = novo

