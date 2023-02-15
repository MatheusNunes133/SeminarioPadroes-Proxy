from .interface_request import Request

class Access(Request):

    def request(self):
        print("Cliente acessou o site!")
