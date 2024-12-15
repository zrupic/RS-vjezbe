'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

print(prvi_i_zadnji(lista))'''

'''lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def maks_i_min(lista):
    min=lista[0]
    maks=lista[0]
    
    for broj in lista:
        if broj > maks:
            maks=broj
        if broj < min:
            min=broj   
    return (maks, min)         
print(maks_i_min(lista))'''

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

def presjek(skup_1, skup_2):
    return(skup_1.intersection(skup_2))

print(presjek(skup_1, skup_2))    