import csv
import numpy as np
import os
from query import *

def open_folder_csv():

    pasta = input("Insira o caminho da pasta: ")

    for diretorio, subpasta, arq in os.walk(pasta):
        dados = [] 
        db_name = []
        for a in arq:
            if(a.split(".")[1] == "csv"):       
                with open(pasta + "/" + a, mode='r') as archive:
                    read_csv = csv.reader(archive, delimiter = ",", quotechar = '"')
                    data = [data for data in read_csv]
                    dados.append(np.asarray(data))
                    n = len(archive.name.split("/"))
                    db_name.append(archive.name.split("/")[n-1].split(".")[0])

        query(dados, db_name)            

def open_local_csv():

    arquivo = input("Insira o nome do arquivo: ")

    with open(arquivo, mode='r') as archive:
        dados = [] 
        db_name = []
        read_csv = csv.reader(archive, delimiter = ",", quotechar = '"')
        data = [data for data in read_csv]
        dados.append(np.asarray(data))
        db_name = archive.name.split(".")[0]
        query(dados, db_name)