## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA

from buscas.busca_from import *
from buscas.busca_where import *
from buscas.busca_order import *
from buscas.busca_dados import *
from buscas.busca_tabelas import *
from buscas.busca_colunas import *
from buscas.busca_coluna import *

def realizaConsulta(dados, tabelas, is_arq):

    query = input("Insira a consulta SQL: ")    

    if(not is_arq):

        fonte = buscaFrom(query)
        condicao = buscaWhere(query)
        ordernacao = buscaOrder(query)

        if(fonte[0]):
            tab = buscaTabelas(tabelas, query, fonte[1])
            col = buscaColunas(query, fonte[1])
            data = buscaDados(dados, tab)

            if(condicao[0]):
                print()

            if(ordernacao[0]):
                print() 

            if(col[1] == 1):
                # select * from employees
                if(col[0][0] == "*"):
                    for d in data:
                        print(d)
                # select emp_no from employees
                else:
                    indice = buscaIndiceColuna(data, col)
                    for d in data:
                        print(d[indice])
                    

            # select emp_no from employees

            # select * from employees order by emp_no desc/asc

            # select emp_no from employees order by emp_no desc/asc
            
            # select emp_no from employees where emp_no = 10001

            # select emp_no from employees where emp_no = 10001 order by emp_no desc/asc
            
            # select emp_no from employees where emp_no = 10001 or emp_no = 10002

            # select emp_no from employees where emp_no = 10001 or emp_no = 10002 order by emp_no desc/asc
            
            # select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02"

            # select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02" order by emp_no desc/asc
    else:
        
        fonte = buscaFrom(query)
        condicao = buscaWhere(query)
        ordernacao = buscaOrder(query)

        if(fonte[0]):

            col = buscaColunas(query, fonte[1])

            if(condicao[0]):
                print()

            if(ordernacao[0]):
                print() 
        
            if(col[1] == 1):
                # select * from employees
                if(col[0][0] == "*"):
                    for d in data:
                        print(d)
                # select emp_no from employees
                else:
                    indice = buscaIndiceColuna(data, col)
                    for d in data:
                        print(d[indice])

            # select * from employees order by emp_no desc/asc
            # select emp_no from employees order by emp_no desc/asc
            
            # select emp_no from employees where emp_no = 10001
            # select emp_no from employees where emp_no = 10001 order by emp_no desc/asc
            
            # select emp_no from employees where emp_no = 10001 or emp_no = 10002
            # select emp_no from employees where emp_no = 10001 or emp_no = 10002 order by emp_no desc/asc
            
            # select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02"
            # select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02" order by emp_no desc/asc