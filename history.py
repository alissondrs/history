from enum import Enum

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
    intro = '/home/alissonsilva/scripts/python/objeto/tcc/textos/intro.txt'

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
        return 'Guerreiiro'
        
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
        return 'Besta'        
    
    def frase_efeito(self):
       return f'Se correr o bicho pega, Se ficar o bicho come'

class Historia_completa():
    # lista = []
    def __init__(self, inicio, meio, lista):
        self._inicio = inicio
        self._meio = meio
        self._lista = lista
    def add_lista(self):
        self._lista.append(self._inicio)
        self._lista.append(self._meio)
    def __str__(self):
        return f'{self._lista}'         
        


class Historia():
    def __init__(self, texto_meio, texto_fim_feliz, texto_fim_triste):
        self._texto_meio = texto_meio
        self._final_feliz = texto_fim_feliz
        self._final_triste = texto_fim_triste

        print(self._texto_meio)
        self._continua = (input("Qual a opção: "))
    def continua(self):    
        if self._continua == '1':
            print(self._final_feliz)
            return self._final_feliz
        elif self._continua == '2':
            print(self._final_triste)
            return self._final_triste
    def __str__(self):         
        return self._final_feliz  


       
class Start():
    guerriro = Guerreiro()
    mago = Mago()
    besta = Besta()
    intro = Ler(Textos.intro.value) 
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
    lista = []
    print(intro)

    escolha=(input('\nEscolha um Personagem:\n 1 - Guerreiro \n 2 - Mago \n 3 - besta \n'))

    if escolha == '1':
        nome = (input("Nome Guerreiro: "))
        personagem = Personagem(nome, guerriro)
        print(personagem)
        print(inicio_guerreiro)
        print('\nPois é nobre guerreiro '+personagem._nome+' sempre tem alguem pra tirar a sua paz\n')
        historia = Historia(meio_guerreiro,fim_feliz_guerreiro, fim_triste_guerreiro)
        # historia.continua()
        final = historia.continua()
        lista.append(inicio_guerreiro.__str__)
        lista.append(final.__str__)
        print(lista)

    elif escolha == '2':    
        nome = (input("Nome Mago: "))
        personagem = Personagem(nome, mago)
        print(personagem)
        print(inicio_mago)
        print('\nVocê gosta de por fogo no parquinho né '+personagem._nome+' seu sem vergonha\n')
        historia = Historia(meio_mago,fim_feliz_mago, fim_triste_mago)
        historia.continua()
       
    elif escolha == '3':        
        nome = (input("Nome Besta: "))
        personagem = Personagem(nome, besta)
        print(personagem)
        print(inicio_besta)
        print('\n Fala  ai '+personagem._nome+' Namastê ou VaiSefudê?  \n')
        historia = Historia(meio_besta,fim_feliz_besta, fim_triste_besta)
        historia.continua()
    else:
        pass

start = Start()