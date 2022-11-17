#entidade serve para chamar o nome da coluna em outra parte do codigo

class EstagiarioOrigem():
    def __init__(self, origem):
        self.__origem = origem


    #coluna origem
    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self, origem):
        self.__origem = origem

#Para cada coluna deve ser criado essa estrutura de @property e @coluna.setter