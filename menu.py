## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA

from listar_tabelas import *
from consulta import *

def menu(dados, tabelas, is_arq):
    while(True):
        print("======================================")
        print("\n (1) Visualizar as tabelas criadas")
        print("\n (2) Inserir a consulta SQL")
        print("\n (3) Voltar para o módulo anterior")
        print("\n (4) Encerrar o programa")
        print("\n======================================")

        opcao = input("Insira a opcao desejada: ")

        if(opcao == str(1)):

            listarTabelas(tabelas, is_arq)
        
        elif(opcao == str(2)):

            realizaConsulta(dados, tabelas, is_arq)
        
        elif(opcao == str(3)):

            return False
        
        elif(opcao == str(4)):
        
            exit()