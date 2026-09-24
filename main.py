from sala import Sala
from evento import EventoShow, FilmeCinema, EventoEsportivo
from ingresso import IngressoInteira, IngressoMeia, IngressoVip
from cliente import Cliente
from venda import Venda

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
    print(f"Preço básico: R$ {evento.preco_basico:.2f}")
    print()

assento1 = sala_show.buscar_assento("A1")
assento2 = sala_show.buscar_assento("A2")
assento3 = sala_show.buscar_assento("A3")

inteira = IngressoInteira("ING001", show, assento1)

meia = IngressoMeia(
    "ING002",
    show,
    assento2,
    "DOC123"
)

vip = IngressoVip(
    "ING003",
    show,
    assento3,
    80.00
)

ingressos = [inteira, meia, vip]
for ingresso in ingressos:
    print(ingresso.emitir_comprovante())
    print()
cliente = Cliente(
    "Felipe",
    "123.456.789-00",
    "felipe@email.com")

venda = Venda(1, cliente)
venda.adicionar_ingresso(inteira)
venda.adicionar_ingresso(meia)
venda.adicionar_ingresso(vip)
print(venda.exibir_recibo())
print("A1 antes:", assento1.status)
venda.confirmar_pagamento()
print("A1 depois:", assento1.status)
print()
print(venda.exibir_recibo())