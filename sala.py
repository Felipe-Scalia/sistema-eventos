from assento import Assento

class Sala:
    def __init__(self, nome, quantidade_fileiras, assentos_por_fileira):
        self.__nome = nome
        self.__quantidade_fileiras = quantidade_fileiras
        self.__assentos_por_fileira = assentos_por_fileira
        self.__capacidade = quantidade_fileiras * assentos_por_fileira
        self.__assentos = []
        self.criar_assentos()

    def criar_assentos(self):
        for i in range(self.__quantidade_fileiras):
            fileira = chr(65 + i)
            for numero in range(1, self.__assentos_por_fileira + 1):
                assento = Assento(fileira, numero)
                self.__assentos.append(assento)

    def buscar_assento(self, codigo):
        for assento in self.__assentos:
            if assento.obter_codigo() == codigo:
                return assento

        return None

    def assentos_disponiveis(self):
        disponiveis = []

        for assento in self.__assentos:
            if assento.esta_livre():
                disponiveis.append(assento)
        return disponiveis

    def capacidade_disponivel(self):
        return len(self.assentos_disponiveis())