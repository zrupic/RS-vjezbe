#zadatak 1

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, God. proizvodnje: {self.godina_proizvodnje}, Prijeđeni km: {self.kilometraza} km")

    def starost(self, trenutna_godina):
        print(f"Automobil je star {trenutna_godina - self.godina_proizvodnje} godina.")
auto = Automobil ("Kia", "ceed", 2020, 55000)

print(auto.ispis())
print(auto.starost(2024))

#zadatak 2

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def zbroj(self):
        return self.a + self.b
    def oduzimanje(self):
        return self.a - self.b
    def mnozenje(self):
        return self.a * self.b
    def dijeljenje(self):
        return self.a / self.b
    def potenciranje(self):
        return self.a ** self.b
    def korijen(self):
        return self.a ** (1 / self.b)
    
digitron = Kalkulator (12, 3)

print("Zbroj:", digitron.zbroj())
print("Oduzimanje:", digitron.oduzimanje())
print("Množenje:", digitron.mnozenje())
print("Dijeljenje:", digitron.dijeljenje())
print("Potenciranje:", digitron.potenciranje())
print("Korijen:", digitron.korijen())
        
#zadatak 3        
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())

print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}, Prosjek: {najbolji_student.prosjek():.2f}")

 #zadatak 4

class Krug:
    def __init__(self, r):
        self.r = r
    def opseg(self):
        return 2 * 3.14 * self.r
    def povrsina(self):
        return 3.14 * self.r ** 2

krug = Krug(7)

print(f"Opseg kruga: {krug.opseg():.2f}")
print(f"Površina kruga: {krug.povrsina():.2f}")

#zadatak 5

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        return f"Radim na poziciji {self.pozicija}"

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)  
        self.department = department

    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        return f"Radnik {radnik.ime} sada ima plaću: {radnik.placa}"


radnik = Radnik("Ivan", "Programer", 7000)


manager = Manager("Žana", "Voditelj", 10000, "IT")

print(radnik.work())  
print(manager.work())  

print(manager.give_raise(radnik, 1000)) 

