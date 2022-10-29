## AUTHOR: GABRIEL DE OLIVEIRA FREIRE SILVA

def buscaWhere(query):
    try:
        pos_where = query.split(" ").index("where")
    except:
        return False, 0
    
    return True, pos_where