class Assento:
    def __init__(self, fileira, numero):
        self.__fileira = fileira
        self.__numero = numero
        self.__status = "livre"

    @property
    def status(self):
        return self.__status

    def ocupar(self):
        self.__status = "ocupado"

    def liberar(self):
        self.__status = "livre"

    def esta_livre(self):
        return self.__status == "livre"

    def obter_codigo(self):
        return f"{self.__fileira}{self.__numero}"