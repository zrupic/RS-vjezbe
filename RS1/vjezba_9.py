lista=[14, 5, 68, 9, 14, 35, 58, 69, 35, 5, 47]
def ukloni(lista):
    return list(set(lista))
nova_lista=ukloni(lista)
print(nova_lista)