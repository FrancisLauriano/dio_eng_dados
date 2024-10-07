from time import sleep
import os

def limpar_terminal():
    sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar_execucao():
    input('\nPressione ENTER para continuar... ') 

