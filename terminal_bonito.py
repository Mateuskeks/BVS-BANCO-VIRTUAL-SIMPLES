#Importaçoes de blibiotecas
import pyfiglet
import os
import pyfiglet
 #Rich
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import print
 #Textual
from textual.app import App
from textual.widgets import Header, Footer, Static
 #Prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

#Limpar o terminal
os.system('clear')

po = False
#Variaveis das senhas
#OBSERVAÇAO : Criar um lugar pra armazenar e criptografar
senha_adm2 = '08082009'
sem_senha = ""
senha_adm_principal = 'roxer987'

#Outras variaveis
console = Console()
bvs_grande = pyfiglet.figlet_format("BVS")

#Funçoes
 #Iniciar o sistema : futuramente adicionar verificaçoes
def iniciar():
    janela_1()

 #Janela Para Mostrar o banco 
def janela_1():
   print("[bold magenta]BEM-VINDO AO BANCO VIRTUAL SIMPLES ![/bold magenta]")
   print(f"[bold magenta]{bvs_grande}[/bold magenta]")

   table = Table(title="Opçoes")
   
   table.add_column("Nome", style="green", no_wrap=True)
   table.add_column("Funçao", style="magenta")
   
   table.add_row("Sair", "Sair do Terminal")
   table.add_row("Entrar", "Entrar no Terminal")

   console.print(table)
   entrou()

   
 #Verificar as senhas
def pedir_senha():

   senha = input('Digite sua senha: ')
   if senha == senha_adm2:
      os.system('clear')
      print('Agora voce tem acesso a parte do sistema')
      sistema_adm()
   elif senha == senha_adm_principal:
      os.system('clear')
      print('[bold green]Ola seja Bem-Vindo ao sistema completo[/bold green]')
      root_adm()
   else:
        print("[italic red]Digite um comando Valido[/italic red]")

 #Entrar ou opçao para entrar
def entrou():
   po = True
   comandos = ["entrar", "sair"]
   completer = WordCompleter(comandos, ignore_case=True)
   while po:
       comando = prompt("Entrar: ", completer=completer).strip().lower()
       if comando == "sair":
           print("Saindo...")
           break

       elif comando == "entrar":
           print("Você escolheu entrar.")
           pedir_senha()

       else:
           print("Comando inválido. Use TAB para autocompletar.")

def sistema_adm():
    print("[italic blue]Bem-Vindo a o BVS[/italic blue]")


def root_adm():

    comandos = ["mudar-senha-adm","mudar-senha-adm-principal","sair","cor-titulo-bvs"]
    completer = WordCompleter(comandos,ignore_case=True)
    while True:
        comando = prompt("Comando Root: ",completer=completer).strip().lower()
        if comando == "sair":
            p=False
            print("[italic red]Voce Saiu ![/italic red]")
            break
        else:
            print("invalido")    



iniciar()