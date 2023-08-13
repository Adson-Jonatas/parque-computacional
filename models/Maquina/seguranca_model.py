class Seguranca:

    __doc__ = 'Classe responsável pelo objeto SEGURANÇA, onde ' \
              'será instanciado o obj de segurança.'

    def __init__(self, lacre):
        self.__lacre = lacre
        print('Segurança criada com sucesso! ')  # LEMBRAR DE COMENTAR ESSE PRINT!

    @property
    def lacre(self):
        return self.__lacre

    @lacre.setter
    def tipo(self, novo):
        self.__lacre = novo
