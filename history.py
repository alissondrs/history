from enum import Enum
class Textos(Enum):
    intro_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro/intro_guerreiro.txt'
    intro_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro/intro_mago.txt'
    intro_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro/intro_besta.txt'
    
class Personagem():
    def __init__(self, nome, tipo):
        self._nome= nome
        self._tipo= tipo
        

    def nome_personagem(self):
        return f'{self._nome}'

    def tipo_personagem(self):
        return f'{self._tipo}'
    

    def __str__(self):
        return f' Nome: {self._nome}\n {self._tipo}'    

class Tipo_personagem():
    def __init__(self):
        pass
        # self._tipo = tipo
     
    def add_arma(self):
        raise Exception()
    
    def add_defesa(self):
        raise Exception()
    
    def add_tipo(self):
        raise Exception()

    def descricao(self):
        raise Exception()

    def add_intro(self):
        raise Exception()    

    def __str__(self):
        return f'Tipo: {self.add_tipo()} \n Arma: {self.add_arma()} Defesa: {self.add_defesa()} \n Descrição: {self.descricao()} \n Intro: {self.add_intro()}'
    
class Guerreiro(Tipo_personagem):
    
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Espada'
        self._defesa = 'Escudo'
        
        
    def add_arma(self):
        return f'{self._arma}' 

    def add_defesa(self):
        return f'{self._defesa}'

    def add_tipo(self):
        return 'Guerreiiro'
    
    def add_intro(self):
        file = Textos.intro_guerra.value
        f = open(file, 'r')
        self._intro = (f.read())
        return f'{self._intro}'            

    def descricao(self):
        return f'Guerreiiro de fé, Nunca Géla!!\n Coragem, força e sangue nos zóio!!'

class Mago(Tipo_personagem):
    
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Poção que deixa Doidão'
        self._defesa = 'Capa Bate-Volta'
        
    def add_arma(self):
        return f'{self._arma}' 

    def add_defesa(self):
        return f'{self._defesa}'

    def add_tipo(self):
        return 'Mago'        

    def descricao(self):
        return f'Mostra a cara Mr. M!!\n Vem na magia do Pai!!'

    def add_intro(self):
        file = Textos.intro_mago.value
        f = open(file, 'r')
        self._intro = (f.read())
        return f'{self._intro}'        

class Besta(Tipo_personagem):
   
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Garras Avassaladoras'
        self._defesa = 'Pele Blindada'
        
    def add_arma(self):
        return f'{self._arma}' 

    def add_defesa(self):
        return f'{self._defesa}'

    def add_tipo(self):
        return 'Besta'        

    def descricao(self):
        return f'Se correr o bicho pega, Se ficar o bicho come'

    def add_intro(self):
        file = Textos.intro_besta.value
        f = open(file, 'r')
        self._intro = (f.read())
        return f'{self._intro}'                

guerreiro = Guerreiro()
pers1 = Personagem('zé', guerreiro)
print(pers1)

mago = Mago()
pers2 = Personagem('jow', mago)
print(pers2)

besta = Besta()
pers3 = Personagem('billy', besta)
print(pers3)

class 