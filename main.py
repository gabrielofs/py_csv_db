## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA
from abre_csv import *

while(True):
    print("Deseja ler um diretório ou uma arquivo na raiz do projeto: \n (1) Diretório \n (2) Arquivo na raiz do projeto \n (3) Para sair")
    opcao = input("Opção: ")

    if(opcao == str(1)):

        ler_diretorio()
    
    elif(opcao == str(2)):
    
        ler_arquivo()

    elif(opcao == str(3)):
    
        exit()