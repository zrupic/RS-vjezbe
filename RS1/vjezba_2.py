# Unos vrijednosti
godina= int(input("Unesite godinu: "))

#petlja
if (godina % 4 ==0 and godina % 100 !=0) or (godina % 400==0):
 print (f"Unešena godina {godina} je prijestupna!")
else:
 print(f"Unešena godina {godina} nije prijestupna!")
