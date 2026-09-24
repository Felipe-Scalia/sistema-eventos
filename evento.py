from abc import ABC, abstractmethod
from sala import Sala


class Evento(ABC):
    def __init__(self, id_evento, titulo, data_hora, preco_basico, sala):
        self.__id_evento = id_evento
        self.__titulo = titulo
        self.__data_hora = data_hora
        self.__preco_basico = preco_basico
        self.__sala = sala

    @property
    def preco_basico(self):
        return self.__preco_basico

    @abstractmethod
    def obter_detalhes(self):
        pass

    @abstractmethod
    def calcular_preco_final(self):
        pass

class EventoShow(Evento):
    def __init__(self, id_evento, titulo, data_hora, preco_basico, sala,
                 artista_banda, genero_artistico, possui_intervalo):

        super().__init__(id_evento, titulo, data_hora, preco_basico, sala)

        self.__artista_banda = artista_banda
        self.__genero_artistico = genero_artistico
        self.__possui_intervalo = possui_intervalo

    def obter_detalhes(self):
        return f"Artista/Banda: {self.__artista_banda}, Gênero: {self.__genero_artistico}, Possui intervalo: {self.__possui_intervalo}"

    def calcular_preco_final(self):
        return self.preco_basico

class FilmeCinema(Evento):
    def __init__(self, id_evento, titulo, data_hora, preco_basico, sala,
                 duracao_min, classificacao_indicativa, formato):

        super().__init__(id_evento, titulo, data_hora, preco_basico, sala)

        self.__duracao_min = duracao_min
        self.__classificacao_indicativa = classificacao_indicativa
        self.__formato = formato

    def obter_detalhes(self):
        return f"Duração: {self.__duracao_min} min, Classificação: {self.__classificacao_indicativa}, Formato: {self.__formato}"

    def calcular_preco_final(self):
        return self.preco_basico

class EventoEsportivo(Evento):
    def __init__(self, id_evento, titulo, data_hora, preco_basico, sala,
                 modalidade, participantes, categoria):

        super().__init__(id_evento, titulo, data_hora, preco_basico, sala)

        self.__modalidade = modalidade
        self.__participantes = participantes
        self.__categoria = categoria

    def obter_detalhes(self):
        return f"Modalidade: {self.__modalidade}, Participantes: {self.__participantes}, Categoria: {self.__categoria}"

    def calcular_preco_final(self):
        return self.preco_basico