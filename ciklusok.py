
#ciklus bizonyos muveletek ismetlesere valo
#ciklusvaltozo - szamlalja hanyszor fut le a ciklus
#ciklusmag - ismetlodo
#ciklusfeltetel - itt adjuk meg meddig fusson
"""
def szamlalosciklus1():
    cv:int = 1

    while (cv <= 10):
        print(f"{cv} Többé nem kések, mert lemaradok fontos infokrol")
        cv += 1

    print(cv, "A ciklus utan")

def elotesztelosciklus():
    #kérj be egy 10-nél nagypbb számot a felhasználótól

    szam: int=int(input("Adjon meg egy 10nel nagyobb szamot"))
    while szam < 10 :
            print("10-nel nagyobb szamot pls")
            szam: int=int(input("Adjon meg egy 10nel nagyobb szamot"))
    print("Hurra vegre sikerult egy szam")


#ird ki a szamokat 1-10 kozott egymas ala
#ird ki a szamokat 20-30 kozott
#ird ki a 15 és 25 kozotti paros szamokat
#ird ki a szamokat egyesevel 12 es 30 kozott forditott sorrendben
"""
kiiras1: int = 1

while (kiiras1 <= 10):
    print(f"{kiiras1}",end=", ")
    kiiras1 += 1
print("\n")

kiiras2: int = 20
while kiiras2 <= 30:
    print(f"{kiiras2}",end=", ")
    kiiras2 += 1
print("\n")

kiiras3: int = 15
while kiiras3 <= 25:
    if kiiras3 % 2 == 0:
        print(f"{kiiras3}",end=", ")
    kiiras3 += 1
print("\n")

kiiras4: int = 30
while kiiras4 >= 12:
    print(f"{kiiras4}",end=", ")
    kiiras4 -= 1
print("\n")