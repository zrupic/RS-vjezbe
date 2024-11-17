def filtriraj_parbr(lista):
    par_br=[broj for broj in lista if broj % 2==0]
    return par_br

lista = [1,2,3,4,5,6,7,8,9,10,11,12]
print (filtriraj_parbr(lista))
