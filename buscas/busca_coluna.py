def buscaIndiceColuna(data, col):
    i = 0
    for d in data[0]:
        if(col[0][0] == d):
            return i
        i += 1