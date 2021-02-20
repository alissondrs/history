from enum import Enum
import os
import time

#Apontar o caminho onde o seu aplicativo vai estar salvo
path = '/home/alissonsilva/scripts/python/objeto/tcc'

#classe responsavel por instancias todos os txts usados.
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

#montando so personagens
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

#crinado um leitor de arquivos de texto
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

#montando a forma de personagens
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

# definindo as caracterristicas de car personagem com herança    
class Guerreiro(Tipo_personagem):
    
    def __init__(self):
        Tipo_personagem.__init__(self)
        self._arma = 'Espada'
        self._defesa = 'Aramadura'
        
        
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
       return f'Vem na Magia do pai que é brisa garantida!!'
 
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
       return f'Na queda ou na ascensão minha atitude vai além, eu tenho disposição pro mal e pro bem'

#montando a impressão da historia completa
class Historia_completa():
    def __init__(self, lista):
        self._lista = lista
        self._tamanho = len(lista)
    def historia(self):
        for i in range(0, self._tamanho, 1):
            print(self._lista[i])
          

#recebendo os textos que dão possibilidade de escolher por qual caminho a se seguir
class Historia():
    def __init__(self, texto_inicio, dialogo, resposta, texto_meio, texto_fim_feliz, texto_fim_triste, lista):
        self._texto_inicio = texto_inicio
        self._texto_meio = texto_meio
        self._final_feliz = texto_fim_feliz
        self._final_triste = texto_fim_triste
        self._dialogo = dialogo
        self._resposta = resposta
        self._lista = lista

        print(self._texto_inicio)
        self._lista.append(self._texto_inicio)
        time.sleep(1.5)
        print(self._dialogo)
        self._lista.append(self._dialogo)
        time.sleep(1.5)
        print(self._resposta)
        self._lista.append(self._resposta)
        time.sleep(1.5)
        print(self._texto_meio)
        time.sleep(1.5)
        self._lista.append(self._texto_meio)
        self._continua = (input("\n\nQual a opção: "))
    def continua(self):    
        if self._continua == '1':
            print(self._final_feliz)
            self._lista.append(self._final_feliz)
        elif self._continua == '2':
            print(self._final_triste)
            self._lista.append(self._final_triste)

#classe responsável por montar o fluxo das historias
class Monta_historia():

    def __init__(self, nome, inicio, lista, tipo, dialogo, resposta, meio, final_feliz, final_triste):
        self._nome = nome
        self._inicio = inicio
        self._lista = lista
        self._tipo = tipo
        self._meio = meio
        self._final_feliz = final_feliz
        self._final_triste = final_triste
        self._dialogo = dialogo
        self._resposta = resposta
    
    def sequencia(self):
        time.sleep(1.5)
        personagem = Personagem(self._nome, self._tipo)
        time.sleep(1.5)
        print(personagem)
        time.sleep(1.5)
        historia = Historia(self._inicio, self._dialogo, self._resposta, self._meio, self._final_feliz, self._final_triste, self._lista)
        historia.continua()
        time.sleep(1.5)
        os.system('clear')
        print('\nHistoria completa\n')
        time.sleep(1.5)
        historia_completa = Historia_completa(self._lista)
        historia_completa.historia()

#funçõ que intancia todas as demais classes e variaveis e monta a historia.     
def Start():

    guerreiro = Guerreiro()
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
    time.sleep(1.0)

    escolha=(input('\nEscolha um Personagem:\n 1 - Guerreiro \n 2 - Mago \n 3 - besta \n'))

    if escolha == '1':
        nome = (input("Nome Guerreiro: "))
        dialogo_guerreiro = '\nNarrador diz: Pois é nobre Guerreiro '+nome+' sempre tem alguem pra tirar a sua paz...\n'
        resposta_guerreiro = 'Guerreiro responde: '+guerreiro.frase_efeito()+'\n'
        monta_historia = Monta_historia(nome, inicio_guerreiro, lista, guerreiro, dialogo_guerreiro, resposta_guerreiro, meio_guerreiro, fim_feliz_guerreiro, fim_triste_guerreiro)
        monta_historia.sequencia()
     

    elif escolha == '2':    
        nome = (input("Nome Mago: "))
        dialogo_mago = ('\nNarrador diz: Você gosta de por fogo no parquinho né Mago '+nome+' seu sem vergonha\n')
        resposta_mago = ('\nMago responde: '+mago.frase_efeito()+'\n')
        monta_historia= Monta_historia(nome, inicio_mago, lista, mago, dialogo_mago, resposta_mago,meio_mago, fim_feliz_mago, fim_triste_mago) 
        monta_historia.sequencia()
        
    elif escolha == '3':        
        nome = (input("Nome besta: "))
        dialogo_besta = ('Narrador diz: Fala ai '+nome+' o humor do dia esta mais pra Namastê ou VaiSefudê?  \n')
        resposta_besta = ('Mago responde: '+besta.frase_efeito()+'\n')
        monta_historia = Monta_historia(nome, inicio_besta, lista, besta, dialogo_besta, resposta_besta, meio_besta, fim_feliz_besta, fim_triste_besta)
        monta_historia.sequencia()

    else:
        pass

start = Start()