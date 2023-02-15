class Client():
    
    def __init__(self, name:str, age:int) -> None:
        self.__name = name
        self.__age = age
    
    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name
    