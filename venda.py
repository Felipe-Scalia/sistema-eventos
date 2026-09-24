class Venda:
    def __init__(self, id_venda, cliente):
        self.__id_venda = id_venda
        self.__cliente = cliente
        self.__ingressos = []
        self.__status_pagamento = "pendente"
        
    def adicionar_ingresso(self, ingresso):
        self.__ingressos.append(ingresso)

    def remover_ingresso(self, ingresso):
        if ingresso in self.__ingressos:
            self.__ingressos.remove(ingresso)

    def calcular_total(self):
        total = 0
        for ingresso in self.__ingressos:
            total += ingresso.calcular_preco()
        return total
    
    def confirmar_pagamento(self):
        self.__status_pagamento = "pago"

        for ingresso in self.__ingressos:
            ingresso.ocupar_assento()

    def cancelar_pagamento(self):
        self.__status_pagamento = "cancelado"

    def exibir_recibo(self):
        return (
            f"----- RECIBO DA VENDA -----\n"
            f"Venda: {self.__id_venda}\n"
            f"Cliente: {self.__cliente.nome}\n"
            f"Quantidade de ingressos: {len(self.__ingressos)}\n"
            f"Total: R$ {self.calcular_total():.2f}\n"
            f"Pagamento: {self.__status_pagamento}")