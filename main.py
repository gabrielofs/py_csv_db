## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA
from open_csv import *

while(True):
    print("Deseja ler um diretório ou uma arquivo na raiz do projeto: \n (1) Diretório \n (2) Arquivo na raiz do projeto")
    opcao = input("Opção: ")

    if(opcao == str(1)):
        open_folder_csv()
    else:
        open_local_csv()

    

# select * from employees

# select emp_no from employees

# select * from employees order by emp_no desc/asc
# select emp_no from employees order by emp_no desc/asc

# select emp_no from employees where emp_no = 10001
# select emp_no from employees where emp_no = 10001 order by emp_no desc/asc

# select emp_no from employees where emp_no = 10001 or emp_no = 10002
# select emp_no from employees where emp_no = 10001 or emp_no = 10002 order by emp_no desc/asc

# select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02"
# select emp_no from employees where emp_no = 10001 and birth_date = "1953-09-02" order by emp_no desc/asc

