from abc import ABC, abstractmethod
from evento import Evento
from assento import Assento

class Ingresso(ABC):
    def __init__(self, codigo_ingresso, evento, assento):
        self._codigo_ingresso = codigo_ingresso
        self._evento = evento
        self._assento = assento

    def ocupar_assento(self):
        self._assento.ocupar()
    
    def emitir_comprovante(self):
        return (
            f"----- COMPROVANTE -----\n"
            f"Ingresso: {self._codigo_ingresso}\n"
            f"Evento: {self._evento.titulo}\n"
            f"Assento: {self._assento.obter_codigo()}\n"
            f"Preço: R$ {self.calcular_preco():.2f}")
    
    @abstractmethod
    def calcular_preco(self):
        pass

class IngressoInteira(Ingresso):
    def calcular_preco(self):
        return self._evento.preco_basico

class IngressoMeia(Ingresso):
    def __init__(self, codigo_ingresso, evento, assento, doc_estudante):
        super().__init__(codigo_ingresso, evento, assento)
        self._doc_estudante = doc_estudante
    def calcular_preco(self):
        return self._evento.preco_basico * 0.5

class IngressoVip(Ingresso):
    def __init__(self, codigo_ingresso, evento, assento, acrescimo_vip):
        super().__init__(codigo_ingresso, evento, assento)
        self._acrescimo_vip = acrescimo_vip
    def calcular_preco(self):
        return self._evento.preco_basico + self._acrescimo_vip