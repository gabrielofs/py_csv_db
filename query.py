
def query(dados, tabelas):
    # select * from employees
    query = input("Insira a consulta: ")

    try:
        pos_from = query.split(" ").index("from")
    except:
        print("O parâmetro from não foi inserido")
        return 0
    
    print(pos_from)

    try:
        pos_where = query.split(" ").index("where")
    except:
        print()
           
    try:
        pos_order = query.split(" ").index("order")
    except:
        print()

    for t in tabelas:
        print(query.split(" ")[pos_from+1])
        if(t == str(query.split(" ")[pos_from+1])):
            print(t)
            pos_dados = tabelas.index(t)
            print(pos_dados)
            for d in dados[pos_dados]:
                print(d)
    