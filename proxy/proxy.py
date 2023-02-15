from .client import Client
from .realizar_compra import Realizar_Compra
from .interface_compra import Interface_Compra

class Proxy_Compra(Interface_Compra):

    def __init__(self, client:Client) -> None:
        self.cliente = client
        self.compra = Realizar_Compra()
    
    def realizar_compra(self):
        client_age = self.cliente.get_age()

        if(client_age >= 18):
            self.compra.realizar_compra()
            print(f"Compra registrada para o cliente {self.cliente.get_name()}")
        else:
            print("O Cliente precisa ser maior de idade para realizar a compra!")
