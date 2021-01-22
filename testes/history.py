from enum import Enum
import os
import time
path = '/home/alissonsilva/scripts/python/objeto/tcc' 
class Textos(Enum):
    
    intro_guerra = ''+path+'/textos/intro_guerreiro.txt'
    intro_mago = ''+path+'/textos/intro_mago.txt'
    intro_besta = ''+path+'/textos/intro_besta.txt'
    inicio_guerra = ''+path+'/textos/inicio_guerreiro.txt'
    inicio_mago = ''+path+'/textos/inicio_mago.txt'
    inicio_besta = ''+path+'/textos/inicio_besta.txt'
    meio_guerra = ''+path+'/textos/meio_guerreiro.txt'
    meio_besta = ''+path+'/textos/meio_besta.txt'
    meio_mago = ''+path+'/textos/meio_mago.txt'
    fim_feliz_guerra = ''+path+'/textos/fim_feliz_guerreiro.txt'
    fim_feliz_besta = ''+path+'/textos/fim_feliz_besta.txt'
    fim_feliz_mago = ''+path+'/textos/fim_feliz_mago.txt'
    fim_triste_guerra = ''+path+'/textos/fim_triste_guerreiro.txt'
    fim_triste_besta = ''+path+'/textos/fim_triste_besta.txt'
    fim_triste_mago = ''+path+'/textos/fim_triste_mago.txt'
    intro = ''+path+'/textos/intro.txt'

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


class Ler():

    def __init__(self, texto):
        self._texto = texto
        
    
    
    def leitor(self):
        file = self._texto
        f = open(file, 'r')
        f.seek(0)
        return f.read()
        
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

    def frase_efeito(self):
        raise Exception()

     
    
    def __str__(self):
        return f'Tipo: {self.add_tipo()} \n Arma: {self.add_arma()} Defesa: {self.add_defesa()} \n Frase de efeito: {self.frase_efeito()}'
    
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
        return 'Guerreiro'
        
    def frase_efeito(self):
        return f'Espada na Caveira!!'

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
           

    def frase_efeito(self):
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
        return 'besta'        
    
    def frase_efeito(self):
       return f'Se correr o bicho pega, Se ficar o bicho come'

class Historia_completa():
    # lista = []
    def __init__(self, lista):
        self._lista = lista
        self._tamanho = len(lista)
    def historia(self):
        for i in range(0, self._tamanho, 1):
            print(self._lista[i])
    # def __str__(self):
    #     return f'{self._lista}'         
        
class Inicio():
    def __init__(self, texto, lista):
        self._texto = texto
        self._lista = lista
    def add_lista(self):
        self._lista.append(self._texto)
    def __str__(self):
        return f'{self._texto}'

class Historia():
    def __init__(self, texto_meio, texto_fim_feliz, texto_fim_triste, lista):
        self._texto_meio = texto_meio
        self._final_feliz = texto_fim_feliz
        self._final_triste = texto_fim_triste
        self._lista = lista

        print(self._texto_meio)
        self._lista.append(self._texto_meio)
        self._continua = (input("\n\nQual a opção: "))
    def continua(self):    
        if self._continua == '1':
            print(self._final_feliz)
            self._lista.append(self._final_feliz)
        elif self._continua == '2':
            print(self._final_triste)
            self._lista.append(self._final_triste)
    def __str__(self):         
        return self._final_feliz  


       
# class Start():
#     guerreiro = Guerreiro()
#     mago = Mago()
#     besta = besta()
#     intro = Ler(Textos.intro.value) 
#     inicio_guerreiro = Ler(Textos.inicio_guerra.value)
#     inicio_mago = Ler(Textos.inicio_mago.value)
#     inicio_besta = Ler(Textos.inicio_besta.value)
#     meio_guerreiro = Ler(Textos.meio_guerra.value)
#     meio_mago = Ler(Textos.meio_mago.value)
#     meio_besta = Ler(Textos.meio_besta.value)
#     fim_feliz_guerreiro = Ler(Textos.fim_feliz_guerra.value)
#     fim_triste_guerreiro = Ler(Textos.fim_triste_guerra.value)
#     fim_feliz_mago = Ler(Textos.fim_feliz_mago.value)
#     fim_triste_mago = Ler(Textos.fim_triste_mago.value)
#     fim_feliz_besta = Ler(Textos.fim_feliz_besta.value)
#     fim_triste_besta = Ler(Textos.fim_triste_besta.value)
#     lista = []


#     print(intro)
#     time.sleep(1.0)

#     escolha=(input('\nEscolha um Personagem:\n 1 - Guerreiro \n 2 - Mago \n 3 - besta \n'))

#     if escolha == '1':
#         nome = (input("Nome Guerreiro: "))
#         time.sleep(0.5)
#         personagem = Personagem(nome, guerreiro)
#         time.sleep(0.5)
#         print(personagem)
#         time.sleep(0.5)
#         inicio = Inicio(inicio_guerreiro, lista)
#         time.sleep(0.5)
#         inicio.add_lista()
#         time.sleep(0.5)
#         print(inicio_guerreiro)
#         time.sleep(0.5)
#         print('\nPois é nobre guerreiro '+personagem._nome+' sempre tem alguem pra tirar a sua paz...\n')
#         time.sleep(0.5)
#         historia = Historia(meio_guerreiro,fim_feliz_guerreiro, fim_triste_guerreiro, lista)
#         time.sleep(0.5)
#         historia.continua()
#         time.sleep(5.0)
#         os.system('clear')
#         print('\nHistoria completa\n')
#         time.sleep(1.5)
#         Historia_completa = Historia_completa(lista)
#         Historia_completa.historia()

#         # tamanho = len(lista)
#         # for i in range(0,tamanho, 1):
#         #     print(lista[i])

#     elif escolha == '2':    
#         nome = (input("Nome Mago: "))
#         time.sleep(0.5)
#         personagem = Personagem(nome, mago)
#         time.sleep(0.5)
#         print(personagem)
#         time.sleep(0.5)
#         inicio = Inicio(inicio_mago, lista)
#         time.sleep(0.5)
#         inicio.add_lista()
#         time.sleep(0.5)
#         print(inicio_mago)
#         time.sleep(0.5)
#         print('\nVocê gosta de por fogo no parquinho né '+personagem._nome+' seu sem vergonha\n')
#         time.sleep(0.5)
#         historia = Historia(meio_mago,fim_feliz_mago, fim_triste_mago, lista)
#         time.sleep(0.5)
#         historia.continua()
#         time.sleep(5.0)
#         print('\nHistoria completa\n')
#         time.sleep(1.5)
#         Historia_completa = Historia_completa(lista)
#         Historia_completa.historia()
        
        
#     elif escolha == '3':        
#         nome = (input("Nome besta: "))
#         time.sleep(0.5)
#         personagem = Personagem(nome, besta)
#         time.sleep(0.5)
#         print(personagem)
#         time.sleep(0.5)
#         inicio = Inicio(inicio_besta, lista)
#         time.sleep(0.5)
#         inicio.add_lista()
#         time.sleep(0.5)
#         print(inicio_besta)
#         time.sleep(0.5)
#         print('\n Fala  ai '+personagem._nome+' Namastê ou VaiSefudê?  \n')
#         time.sleep(0.5)
#         historia = Historia(meio_besta,fim_feliz_besta, fim_triste_besta, lista)
#         time.sleep(0.5)
#         historia.continua()
#         time.sleep(5.0)
#         print('\nHistoria completa\n')
#         time.sleep(1.5)
#         Historia_completa = Historia_completa(lista)
#         Historia_completa.historia()
#     else:
#         pass

# start = Start()





def test_guerreio():
    guerreiro = Guerreiro()
    personagem = Personagem('joão', guerreiro)
    assert personagem.nome_personagem() == 'joão'
    assert guerreiro._arma == 'Espada'
    assert guerreiro._defesa == 'Escudo'
    assert guerreiro.frase_efeito() == 'Espada na Caveira!!'
    # assert guerreiro.add_tipo == 'Guerreiro'

def test_mago():
    mago = Mago()
    personagem = Personagem('joão', mago)
    assert personagem.nome_personagem() == 'joão'
    assert mago._arma == 'Poção verde sintilante que deixa Doidão'
    assert mago._defesa == 'Capa hiponotizante'
    assert mago.frase_efeito() == 'Mostra a cara Mr.M'


def test_besta():
    besta = Besta()
    personagem = Personagem('joão', besta)
    assert personagem.nome_personagem() == 'joão'
    assert besta._arma == 'Garras Avassaladoras'
    assert besta._defesa == 'Pele Blindada'    
    assert besta.frase_efeito() == 'Se correr o bicho pega, Se ficar o bicho come'


def test_tipoPersonagem():
    guerreiro = Guerreiro()
    # personagem = Personagem('joão', guerreiro)
    assert guerreiro.add_arma == 'Espada'