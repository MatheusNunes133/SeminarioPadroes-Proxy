from abc import ABC, abstractclassmethod

class Request(ABC):

    @abstractclassmethod
    def request():
        pass