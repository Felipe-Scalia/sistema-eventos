from sala import Sala
from evento import EventoShow, FilmeCinema, EventoEsportivo


sala_show = Sala("Arena Principal", 5, 10)
sala_cinema = Sala("Sala de Cinema", 4, 8)
sala_esporte = Sala("Ginásio", 6, 10)


show = EventoShow(
    1,
    "Show de Rock",
    "25/09/2026 20:00",
    200.00,
    sala_show,
    "Linkin Park",
    "Rock",
    False
)

filme = FilmeCinema(
    2,
    "Interestelar",
    "26/09/2026 19:00",
    40.00,
    sala_cinema,
    169,
    10,
    "2D"
)

esporte = EventoEsportivo(
    3,
    "Final de Vôlei",
    "27/09/2026 18:00",
    80.00,
    sala_esporte,
    "Vôlei",
    "Time A x Time B",
    "Profissional"
)

eventos = [show, filme, esporte]

for evento in eventos:
    print(evento.obter_detalhes())
    print(f"Preço: R$ {evento.calcular_preco_final():.2f}")
    print()