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
    fim1_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim1_guerreiro.txt'
    fim1_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim1_besta.txt'
    fim1_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim1_mago.txt'
    fim2_guerra = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim2_guerreiro.txt'
    fim2_besta = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim2_besta.txt'
    fim2_mago = '/home/alissonsilva/scripts/python/objeto/tcc/textos/fim2_mago.txt'

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
        # self._tipo = tipo
     
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
        self._arma = 'Poção que deixa Doidão'
        self._defesa = 'Capa Bate-Volta'
        
    def add_arma(self):
        return f'{self._arma}' 

    def add_defesa(self):
        return f'{self._defesa}'

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
        return f'{self._arma}' 

    def add_defesa(self):
        return f'{self._defesa}'

    def add_tipo(self):
        return 'Besta'        
    
    def descricao(self):
       return f'Se correr o bicho pega, Se ficar o bicho come'

class Meio():
    def __init__(self, texto):
        self._texto = texto
        # self._final_feliz = bool
             
        print(self._texto)
        self._continua = (input("Qual a opção: "))
    def continua(self):    
        if self._continua == '1':
            self._final_feliz = False
        else:
            self._final_feliz = True
    def final(self):         
        return self._final_feliz  

class Final():
    def __init__(self, final, finalfeliz, finaltriste):
        self._final = final
        self._finalfeliz = finalfeliz
        self._finaltriste = finaltriste
        
    def final(self):
        if self._final:
            self._fim = Ler(self._finalfeliz)
        else:
            self._fim = Ler(self._finaltriste)

    def fim(self):
        return f'{{{self._fim}}}'                 





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
    fim1_guerreiro = Ler(Textos.fim1_guerra.value)
    fim2_guerreiro = Ler(Textos.fim2_guerra.value)
    fim1_mago = Ler(Textos.fim1_mago.value)
    fim2_mago = Ler(Textos.fim2_mago.value)
    fim1_besta = Ler(Textos.fim1_besta.value)
    fim2_besta = Ler(Textos.fim2_besta.value)
    continua_guerreiro = True
    continua_mago = True
    continua_besta = True
    final_feliz_guerreiro = True
    final_feliz_mago = True
    final_feliz_besta = True


    escolha=(input('Escolha um Personagem:\n 1 - Guerreiro \n 2 - Mago \n 3 - besta \n'))

    if escolha == '1':
        nome = (input("Nome Guerreiro: "))
        personagem = Personagem(nome, guerriro)
        print(personagem)
        # meio = Ler(Textos.meio_guerra.value)
        print(inicio_guerreiro)
        meio = Meio(meio_guerreiro)
        final = Final(meio.final,fim1_guerreiro, fim2_guerreiro)
        fim = final.final
        print(final.fim)
        continua_guerreiro
        continua_mago = False
        continua_besta = False

    elif escolha == '2':    
        nome = (input("Nome Mago: "))
        personagem = Personagem(nome, mago)
        print(personagem)
        print(inicio_mago)
        continua_guerreiro = False
        continua_mago
        continua_besta = False
       
    elif escolha == '3':        
        nome = (input("Nome Besta: "))
        personagem = Personagem(nome, besta)
        print(personagem)
        print(inicio_besta)
        continua_guerreiro = False
        continua_mago = False
        continua_besta

    # if continua_guerreiro:
    #     meio = Meio(meio_guerreiro)
    #     if meio.final == True:
    #         print('final feliz')
    #     else:
    #         print('final triste')     
        
        # continua
        

        # print(meio_guerreiro)
        # continua = (input("Qual a opção: "))
        # if continua == '1':
        #     final_feliz_guerreiro = False
        # else:
        #     final_feliz_guerreiro = True    

    # if final_feliz_guerreiro:
    #     print(fim1_guerreiro)
    
    # if final_feliz_guerreiro == False:
    #     print(fim2_guerreiro)    
    # def meio(self, texto):
    #     self._texto = texto
    #     self._final_feliz = bool
    #     print(self._texto)
    #     self._continua = (input("Qual a opção: "))
    #     if self.continua == '1':
    #         self._final_feliz = False
    #     else:
    #         self._final_feliz = True 
    #     return self._final_feliz     



               

    # def meio(self, personagem):
    #     self.personagem = personagem
    #     self._nome = personagem.nome_personagem()
    #     print(self._nome)

        

    # def meio(self, personagem):
    #     pass

    # def fim(self, personagem):
    #     pass    
        
# start = Start()

# print(meio)

# inicio_war = Textos.inicio_guerra.value
# ler = Ler(inicio_war) 