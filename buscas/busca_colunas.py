## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA

def buscaColunas(query, pos_from):
    i = 1
    count = 0
    colunas = []

    while(i < pos_from):
        colunas.append(query.split(" ")[i])
        count = i
        i += 1
    
    return colunas, count