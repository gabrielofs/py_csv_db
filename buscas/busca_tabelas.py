## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA

def buscaTabelas(tabelas, query, pos_from):    
    for t in tabelas:
        if(t == str(query.split(" ")[pos_from+1])):
            return tabelas.index(t) 