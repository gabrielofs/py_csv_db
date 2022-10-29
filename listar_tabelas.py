def listarTabelas(tabelas, is_arq):
    
    print("\n -----------\n")

    if(not is_arq):
        print("Tabelas criadas: \n")
        for tab in tabelas:
            print("> " + tab)
    else:
        print("Tabela criada: \n")
        print("> " + tabelas)

    print("\n -----------")