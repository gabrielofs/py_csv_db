from buscas.busca_from import *
from buscas.busca_where import *
from buscas.busca_order import *
from buscas.busca_dados import *
from buscas.busca_tabelas import *
from buscas.busca_colunas import *

def realizaConsulta(dados, tabelas):

    query = input("Insira a consulta SQL: ")    

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
    
        # select * from employees
        if(col[1] == 1):
            if(col[0][0] == "*"):
                for d in data:
                    print(d)

        # select emp_no from employees

        # select * from employees order by emp_no desc/asc
        # select emp_no from employees order by emp_no desc/asc
        
        # select emp_no from employees where emp_no = 10001
        # select emp_no from employees where emp_no = 10001 order by emp_no desc/asc
        
        # select emp_no from employees where emp_no = 10001 or emp_no = 10002
        # select emp_no from employees where emp_no = 10001 or emp_no = 10002 order by emp_no desc/asc
        
        # select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02"
        # select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02" order by emp_no desc/asc
