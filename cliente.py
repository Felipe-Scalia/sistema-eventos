class Cliente:
    def __init__(self, nome, cpf, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def email(self):
        return self.__email