import math

a = int(input("Kérlek add meg az a-t: "))
b = int(input("Kérlek add meg az b-t: "))
c = int(input("Kérlek add meg az c-t: "))

diszkriminans = (b * b) - (4*a*c)

if(diszkriminans < 0):
        print("Nincs valós megoldás!")
elif(diszkriminans == 0):
    print("1 megoldása van")
    megoldas = (-1 * b) / (2*a)
    print("Megoldás: ",megoldas)
else:
    print("2 megoldása van")
    gyok_diszk = math.sqrt(diszkriminans)
    megoldas1 = ((-1 * b) + gyok_diszk) / (2*a)
    megoldas2 = ((-1*b) - gyok_diszk) / (2*a)
    print("Megoldás 1: ",megoldas1,"\n Megoldás 2: ",megoldas2)

