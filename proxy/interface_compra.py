from abc import ABC, abstractclassmethod

class Interface_Compra(ABC):

    @abstractclassmethod
    def realizar_compra(self):
        pass