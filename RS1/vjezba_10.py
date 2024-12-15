tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def brojanje_rjeci(tekst):
    rijeci=tekst.split()
    brojac={}

    for rijec in rijeci:
        if rijec in brojac:
            brojac[rijec] +=1
        else:
            brojac[rijec]=1
    return brojac
rezultat=brojanje_rjeci(tekst)
print(rezultat)        
