from proxy.client import Client
from proxy.proxy import Proxy_Compra

#Compra feita por cliente maior de idade
client = Client("Matheus", 20)

proxy = Proxy_Compra(client)
proxy.realizar_compra()

#Compra feita por cliente menor de idade

client_menor = Client("João", 17)
proxy = Proxy_Compra(client_menor)
proxy.realizar_compra()
