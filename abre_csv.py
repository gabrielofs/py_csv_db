import csv
import numpy as np
import os
from consulta import *
from menu import *

def ler_diretorio():

    try: 
    
        pasta = input("Insira o caminho da pasta: ")

        for diretorio, subpasta, arq in os.walk(pasta):
            dados = [] 
            nomes_das_tabelas = []
            for a in arq:
                if(a.split(".")[1] == "csv"):       
                    with open(pasta + "/" + a, mode='r') as archive:
                        ler_csv = csv.reader(archive, delimiter = ",", quotechar = '"')
                        dado = [dado for dado in ler_csv]
                        dados.append(np.asarray(dado))
                        tam_vetor = len(archive.name.split("/"))
                        nomes_das_tabelas.append(archive.name.split("/")[tam_vetor-1].split(".")[0])

            menu(dados, nomes_das_tabelas, False)

    except FileNotFoundError as error:
        print("\n -----------")
        print("\n Exception: " + str(error))
        print("\n -----------\n")

def ler_arquivo():

    arquivo = input("Insira o nome do arquivo: ")

    try:
        with open(arquivo, mode='r') as archive:
            dados = [] 
            nomes_das_tabelas = []
            ler_csv = csv.reader(archive, delimiter = ",", quotechar = '"')
            data = [data for data in ler_csv]
            dados.append(np.asarray(data))
            nomes_das_tabelas = archive.name.split(".")[0]

        menu(dados, nomes_das_tabelas, True)
    
    except FileNotFoundError as error:
        print("\n -----------")
        print("\n Exception: " + str(error))
        print("\n -----------\n")