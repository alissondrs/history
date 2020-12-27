
class Personagem():
    def __init__(self, nome, tipo, skils):
        self._nome= nome
        self._tipo= tipo
        self._skils= skils

    def nome_personagem(self):
        return f'{self._nome}'

    def tipo_personagem(self):
        return f'{self._tipo}'
    
    def skils_personagem(self):
        return f'{self._skils}'

    def __str__(self):
        return f' Nome: {self._nome}\n Tipo: {self._tipo} Skils: {self._skils}'    


pers = Personagem('zé', 'malandro', 'quebra tranca')
print(pers)


