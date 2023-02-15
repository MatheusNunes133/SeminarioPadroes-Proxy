from .client import Client
from .interface_request import Request
from .access import Access

class Proxy_Access(Request):

    def __init__(self, client:Client) -> None:
        self.__client = client
        self.__access = Access()

    def request(self):
        if self.check_access():
            self.log_client()
            self.__access.request()
        else:
            print("O cliente precisa ser maior de idade")
       
    
    def check_access(self) -> bool:
        print("Verificando acesso do Cliente...")
        client_age = self.__client.get_age()

        if client_age >= 18:
            return True
        else:
            return False
    
    def log_client(self):
        print("Cliente conseguiu acesso...")
