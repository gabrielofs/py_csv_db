def buscaFrom(query):
    try:
        pos_from = query.split(" ").index("from")
    except:
        print("O parâmetro from não foi inserido")
        return False, 0
    
    return True, pos_from