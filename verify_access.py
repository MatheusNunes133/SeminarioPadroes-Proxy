from access.client import Client
from access.proxy_access import Proxy_Access

#Acessando site com cliente maior de idade
client = Client("Matheus", 20)
proxy = Proxy_Access(client)
proxy.request()

print("")

#Acessando site com cliente menor de idade
client = Client("João", 17)
proxy = Proxy_Access(client)
proxy.request()
