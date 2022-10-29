def buscaOrder(query):
    try:
        pos_order = query.split(" ").index("order")
    except:
        return False, 0
    
    return True, pos_order