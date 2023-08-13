
class Hardware:

    __doc__ = 'Classe responsável pelo objeto HARDWARE, onde ' \
              'será instanciado o obj de hardware.'

    def __init__(self, placa_mae, mac):
        self.__placa_mae = placa_mae
        self.__mac = mac
        print('Hardware criado com sucesso! ')  # LEMBRAR DE COMENTAR ESSE PRINT!

    @property
    def placa_mae(self):
        return self.__placa_mae

    @placa_mae.setter
    def placa_mae(self, novo):
        self.__placa_mae = novo

    @property
    def mac(self):
        return self.__mac

    @mac.setter
    def mac(self, novo):
        self.__mac = novo
