from enum import Enum
import abc
class Textos(Enum):
    
    intro_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro_guerreiro.txt'
    intro_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro_mago.txt'
    intro_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro_besta.txt'
    inicio_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/inicio_guerreiro.txt'
    inicio_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/inicio_mago.txt'
    inicio_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/inicio_besta.txt'
    meio_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/meio_guerreiro.txt'
    meio_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/meio_besta.txt'
    meio_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/meio_mago.txt'
    fim_feliz_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim_feliz_guerreiro.txt'
    fim_feliz_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim_feliz_besta.txt'
    fim_feliz_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim_feliz_mago.txt'
    fim_triste_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim_triste_guerreiro.txt'
    fim_triste_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim_triste_besta.txt'
    fim_triste_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim_triste_mago.txt'

class Personagem():
    def __init__(self, nome, tipo):
        self._nome= nome
        self._tipo= tipo
        

    def nome_personagem(self):
        return self._nome

    def tipo_personagem(self):
        return self._tipo    

    def __str__(self):
        return f' Nome: {self._nome}\n {self._tipo}'    

class Ler_texto(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def leitor(self):
        return
    def __str__(self):
        return 

class Ler(Ler_texto):

    def __init__(self, texto):
        self._texto = texto
        
    
    
    def leitor(self):
        file = self._texto
        f = open(file, 'r')
        print(f.read())
        
    def __str__(self):
        return f'{self.leitor()}'

class Tipo_personagem():
    def __init__(self):
        pass
      
     
    def add_arma(self):
        raise Exception()
    
    def add_defesa(self):
        raise Exception()
    
    def add_tipo(self):
        raise Exception()

    def descricao(self):
        raise Exception()

     
    
    def __str__(self):
        return f'Tipo: {self.add_tipo()} \n Arma: {self.add_arma()} Defesa: {self.add_defesa()} \n Descrição: {self.descricao()}'
    
class Guerreiro(Tipo_personagem):
    
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Espada'
        self._defesa = 'Escudo'
        
        
    def add_arma(self):
        return self._arma 

    def add_defesa(self):
        return self._defesa

    def add_tipo(self):
        return 'Guerreiiro'
        
    def descricao(self):
        return f'Guerreiiro de fé, Nunca Géla!!\n Coragem, força e sangue nos zóio!!'

class Mago(Tipo_personagem):
    
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Poção verde sintilante que deixa Doidão'
        self._defesa = 'Capa hiponotizante'
        
    def add_arma(self):
        return self._arma 

    def add_defesa(self):
        return self._defesa

    def add_tipo(self):
        return 'Mago'        
           

    def descricao(self):
       return f'Mostra a cara Mr.M'

 
class Besta(Tipo_personagem):
   
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Garras Avassaladoras'
        self._defesa = 'Pele Blindada'
        
    def add_arma(self):
        return self._arma 

    def add_defesa(self):
        return self._defesa

    def add_tipo(self):
        return 'Besta'        
    
    def descricao(self):
       return f'Se correr o bicho pega, Se ficar o bicho come'

class Meio():
    def __init__(self, texto_meio, texto_fim_feliz, texto_fim_triste):
        self._texto_meio = texto_meio
        self._final_feliz = texto_fim_feliz
        self._final_triste = texto_fim_triste

        print(self._texto_meio)
        self._continua = (input("Qual a opção: "))
    def continua(self):    
        if self._continua == '1':
            print(self._final_feliz)
        elif self._continua == '2':
            print(self._final_triste)
    def __str__(self):         
        return self._final_feliz  

         





class Start():

    guerriro = Guerreiro()
    mago = Mago()
    besta = Besta()
    inicio_guerreiro = Ler(Textos.inicio_guerra.value)
    inicio_mago = Ler(Textos.inicio_mago.value)
    inicio_besta = Ler(Textos.inicio_besta.value)
    meio_guerreiro = Ler(Textos.meio_guerra.value)
    meio_mago = Ler(Textos.meio_mago.value)
    meio_besta = Ler(Textos.meio_besta.value)
    fim_feliz_guerreiro = Ler(Textos.fim_feliz_guerra.value)
    fim_triste_guerreiro = Ler(Textos.fim_triste_guerra.value)
    fim_feliz_mago = Ler(Textos.fim_feliz_mago.value)
    fim_triste_mago = Ler(Textos.fim_triste_mago.value)
    fim_feliz_besta = Ler(Textos.fim_feliz_besta.value)
    fim_triste_besta = Ler(Textos.fim_triste_besta.value)



    escolha=(input('Escolha um Personagem:\n 1 - Guerreiro \n 2 - Mago \n 3 - besta \n'))

    if escolha == '1':
        nome = (input("Nome Guerreiro: "))
        personagem = Personagem(nome, guerriro)
        print(personagem)
        print(inicio_guerreiro)
        meio = Meio(meio_guerreiro,fim_feliz_guerreiro, fim_triste_guerreiro)
        meio.continua()

    elif escolha == '2':    
        nome = (input("Nome Mago: "))
        personagem = Personagem(nome, mago)
        print(personagem)
        print(inicio_mago)
        meio = Meio(meio_mago,fim_feliz_mago, fim_triste_mago)
        meio.continua()
       
    elif escolha == '3':        
        nome = (input("Nome Besta: "))
        personagem = Personagem(nome, besta)
        print(personagem)
        print(inicio_besta)
        meio = Meio(meio_besta,fim_feliz_besta, fim_triste_besta)
        meio.continua()
