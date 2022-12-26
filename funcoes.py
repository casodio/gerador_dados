from random import choice
from time import sleep
import os
from time import sleep
from rich import print
from rich.progress import Progress

#CRIANDO ABERTURA DO SISTEMA
print('\n','''
Bem vindo ao Sistema Gerador de dados para teste.
O sistema irá gerar dados aleatorios apenas para teste de funcionamento.

Se gostou do sistema, entra em contato!

##############################################

|--------------------------------------------|
|          Autor - [bold][underline]Marcio Maia[/][/]               |
|*****************[bold]Contatos[/]*******************|
| [bold magenta]E-mail:[/] marciojesusmaia@hotmail.com        |
| [bold cyan]Linkedin:[/] https://www.linkedin.com/in/marciojesusmaia/ |
| [bold green]Telefone/Whatsapp:[/] 55 85 98614-9863        |
|--------------------------------------------|

##############################################''','\n')
input('Pressione < Enter > para prosseguir!')
os.system('clear')



# CRIANDO O MENU DE OPÇÕES A GERAR: NOMES, E-MAILS, TELEFONES, CIDADES, ESTADOS
def menu():
    print('Bem vindo ao gerador de dados teste')
    print('Escolha uma ou mais opçẽs separando por [green]virgula[/].')
    print( 'Se quiser [green]salvar[/] digite "salvar" e todo o historico será salvo.')
    print('Se ja estiver satisfeito com os testes e desejar sair é só digitar [bold red]sair[/] a qualquer momento.','\n')
    print('-'*30)
    print('| Escolha uma ou mais opcoes |')
    print('-'*30)
    print('|','[1]- [purple]Nome'.ljust(34),'|')
    print('|','[2]- [purple]E-mail  '.ljust(34),'|')
    print('|','[3]- [purple]Telefone    '.ljust(34),'|')
    print('|','[4]- [purple]Cidade  '.ljust(34),'|')
    print('|','[5]- [purple]Estado  '.ljust(34),'|')
    print('-'*30)

# CRIANDO A LISTA DE NOMES
nomes = ['Marcio', 'Maia', 'Max', 'Marcelo', 'Gabriela', 'Marcia', 'Rozario', 'Luiza', 'Elizete', 'Eliete', 'Elizabete']
# CRIANDO A LISTA DE E-MAILS
emails = ['marcio@hotmail.com', 'eliz@gmali.com', 'rozario@outlook.com', 'elizabete@chrome.com.br', 'eliete@yahoo.com.br', 'marcelo@bol.com.br']
# CRIANDO A LISTA DE TELEFONES
fones = ['85986149863', '85987671721', '88998331545', '86996532413', '879855476213', '8191478542', '82965348157']
# CRIANDO A LISTA DE CIDADES
cidades = ['Pacatuba', 'Maracanau', 'Pavuna', 'Buenos Aires', 'Nova Iorque', 'Sao Francisco', 'Lima', 'Puno', 'Cairo', 'Lagos']
# CRIANDO A LISTA DE ESTADOS
estados = ['Ceara', 'Santa Catarina', 'Rio de janeiro', 'Arequipa', 'Cusco', 'Sanca Cruz', 'Tarija', 'Chaco', 'Cordova']

textos = []


# FUNCOES DE ESCOLHAS DE TESTE
def escolher():
    escolhas = input('Digite uma ou mais opcoes: ').strip().split(',')
    for escolha in escolhas:
        if escolha == '1':
            print('Nome: ', end='')
            nome()
              
        elif escolha == '2':
            print('Email: ', end='')
            email()
            
        elif escolha == '3':
            print('Telefone: ', end='')
            fone()
            
        elif escolha == '4':
            print('Cidade: ', end='')
            cidade()
            
        elif escolha == '5':
            print('Estado: ', end='')
            estado()

        elif escolha == '':
            print('Ops! não foi digitado nenhuma escola, tente novamente...')
            escolher()

        elif escolha == 'sair':
            sair()
            
        elif escolha not in '12345':
            print(f'Uma ou mais opçẽs [red]digitadas[/] está incorreta.')
            escolher()

# ESCOLHENDO NOME
def nome():
    um = choice(nomes)
    print(um)
    textos.append(um)

# ESCOLHENDO EMAIL
def email():
    dois = choice(emails)
    print(dois)
    textos.append(dois)

# ESCOLHENDO TELEFONES
def fone():
    tres = choice(fones)
    print(tres)
    textos.append(tres)

# ESCOLHENDO CIDADES
def cidade():
    quatro = choice(cidades)
    print(quatro)
    textos.append(quatro)

# ESCOLHENDO ESTADOS

def estado():
    cinco = choice(estados)
    print(cinco)
    textos.append(cinco)


# SAINDO DO SISTEMA
def sair():
    print('\n','Obrigador por testar nosso sistema...')
    sleep(3)
   
    with Progress() as progress:
        taks1 = progress.add_task('[bold red]Saindo...', total = 100)

        while not progress.finished:
            progress.update(taks1,advance=1)
            sleep(0.02)
    exit()

from random import choice
from time import sleep
import os
from time import sleep
from rich import print
from rich.progress import Progress

#CRIANDO ABERTURA DO SISTEMA
print('\n','''
Bem vindo ao Sistema Gerador de dados para teste.
O sistema irá gerar dados aleatorios apenas para teste de funcionamento.

Se gostou do sistema, entra em contato!

##############################################

|--------------------------------------------|
|          Autor - [bold][underline]Marcio Maia[/][/]               |
|*****************[bold]Contatos[/]*******************|
| [bold magenta]E-mail:[/] marciojesusmaia@hotmail.com        |
| [bold cyan]Linkedin:[/] https://www.linkedin.com/in/marciojesusmaia/ |
| [bold green]Telefone/Whatsapp:[/] 55 85 98614-9863        |
|--------------------------------------------|

##############################################''','\n')
input('Pressione < Enter > para prosseguir!')
os.system('clear')



# CRIANDO O MENU DE OPÇÕES A GERAR: NOMES, E-MAILS, TELEFONES, CIDADES, ESTADOS
def menu():
    print('Bem vindo ao gerador de dados teste')
    print('Escolha uma ou mais opçẽs separando por [green]virgula[/].')
    print( 'Se quiser [green]salvar[/] digite "salvar" e todo o historico será salvo.')
    print('Se ja estiver satisfeito com os testes e desejar sair é só digitar [bold red]sair[/] a qualquer momento.','\n')
    print('-'*30)
    print('| Escolha uma ou mais opcoes |')
    print('-'*30)
    print('|','[1]- [purple]Nome'.ljust(34),'|')
    print('|','[2]- [purple]E-mail  '.ljust(34),'|')
    print('|','[3]- [purple]Telefone    '.ljust(34),'|')
    print('|','[4]- [purple]Cidade  '.ljust(34),'|')
    print('|','[5]- [purple]Estado  '.ljust(34),'|')
    print('-'*30)

# CRIANDO A LISTA DE NOMES
nomes = ['Marcio', 'Maia', 'Max', 'Marcelo', 'Gabriela', 'Marcia', 'Rozario', 'Luiza', 'Elizete', 'Eliete', 'Elizabete']
# CRIANDO A LISTA DE E-MAILS
emails = ['marcio@hotmail.com', 'eliz@gmali.com', 'rozario@outlook.com', 'elizabete@chrome.com.br', 'eliete@yahoo.com.br', 'marcelo@bol.com.br']
# CRIANDO A LISTA DE TELEFONES
fones = ['85986149863', '85987671721', '88998331545', '86996532413', '879855476213', '8191478542', '82965348157']
# CRIANDO A LISTA DE CIDADES
cidades = ['Pacatuba', 'Maracanau', 'Pavuna', 'Buenos Aires', 'Nova Iorque', 'Sao Francisco', 'Lima', 'Puno', 'Cairo', 'Lagos']
# CRIANDO A LISTA DE ESTADOS
estados = ['Ceara', 'Santa Catarina', 'Rio de janeiro', 'Arequipa', 'Cusco', 'Sanca Cruz', 'Tarija', 'Chaco', 'Cordova']

textos = []


# FUNCOES DE ESCOLHAS DE TESTE
def escolher():
    escolhas = input('Digite uma ou mais opcoes: ').strip().split(',')
    for escolha in escolhas:
        if escolha == '1':
            print('Nome: ', end='')
            nome()
              
        elif escolha == '2':
            print('Email: ', end='')
            email()
            
        elif escolha == '3':
            print('Telefone: ', end='')
            fone()
            
        elif escolha == '4':
            print('Cidade: ', end='')
            cidade()
            
        elif escolha == '5':
            print('Estado: ', end='')
            estado()

        elif escolha == '':
            print('Ops! não foi digitado nenhuma escola, tente novamente...')
            escolher()

        elif escolha == 'sair':
            sair()
            
        elif escolha not in '12345':
            print(f'Uma ou mais opçẽs [red]digitadas[/] está incorreta.')
            escolher()

# ESCOLHENDO NOME
def nome():
    um = choice(nomes)
    print(um)
    textos.append(um)

# ESCOLHENDO EMAIL
def email():
    dois = choice(emails)
    print(dois)
    textos.append(dois)

# ESCOLHENDO TELEFONES
def fone():
    tres = choice(fones)
    print(tres)
    textos.append(tres)

# ESCOLHENDO CIDADES
def cidade():
    quatro = choice(cidades)
    print(quatro)
    textos.append(quatro)

# ESCOLHENDO ESTADOS

def estado():
    cinco = choice(estados)
    print(cinco)
    textos.append(cinco)


# SAINDO DO SISTEMA
def sair():
    print('\n','Obrigador por testar nosso sistema...')
    sleep(3)
   
    with Progress() as progress:
        taks1 = progress.add_task('[bold red]Saindo...', total = 100)

        while not progress.finished:
            progress.update(taks1,advance=1)
            sleep(0.02)
    exit()


# SALVAR EM ARQUIVO     
def salvar():
    with open('dados_teste.txt', 'a') as test:
        for dado in textos:
            test.write(dado + os.linesep)

# QUER SALVAR?
def salvando():
        salve = input('Deseja salvar os dados em arquivo: ').lower()
        if salve == 'sair':
            sair()

        elif salve == 'nao':
            escolher()

        elif salve == 'salvar':
            salvar()

        elif salve == '':
            print('Se quiser salvar digite "salvar"...')
            salvando()

# SALVAR EM ARQUIVO     
def salvar():
    with open('dados_teste.txt', 'a') as test:
        for dado in textos:
            test.write(dado + os.linesep)

# QUER SALVAR?
def salvando():
        salve = input('Deseja salvar os dados em arquivo: ').lower()
        if salve == 'sair':
            sair()

        elif salve == 'nao':
            escolher()

        elif salve == 'salvar':
            salvar()

        elif salve == '':
            print('Se quiser salvar digite "salvar"...')
            salvando()
