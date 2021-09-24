import random

raw_input_data = input("Adj meg egy számot: ")
try:
    number = int(raw_input_data)  # konvertáljuk át számmá: float("") -valós szám vagy int("") - egész szám vagy str("")
    if number >= 3 and number < 17:
        print("Beleesik a szám a [3, 17) intervallumba.")
    else:
        print("Nem esik bele a [3, 17) intervallumba.")

    a, b, c = 2, 6, 4
    if a + b > c and a + c > b and b + c > a:
        print("Lehet ezen oldalhosszakkal háromszöveg szerkeszteni.")
    else:
        print("Nem lehet ezen oldalhosszakkal háromszöveg szerkeszteni.")

    if a >= b and a >= c and b >= c:
        print(a, "a legnagyobb szám.")
        print(c, "a legkisebb szám.")
    elif a >= b and a >= c and c >= b:
        print(a, "a legnagyobb szám.")
        print(b, "a legkisebb szám.")
    elif b >= a and b >= c and c >= a:
        print(b, "a legnagyobb szám.")
        print(a, "a legkisebb szám.")
    elif c >= a and b >= c and a >= c:
        print(c, "a legnagyobb szám.")
        print(b, "a legkisebb szám.")
    else:
        print(c, "a legnagyobb szám.")
        print(a, "a legkisebb szám.")

    str1 = "-"
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    if maganhangzok.find(str1) >= 0:
        print("A karakter magánhangzó.")
    else:
        print("A karakter nem magánhangzó.")

    irasjelek = ".,-_:?'+!%/="
    szamjegyek = "1234567890"
    if szamjegyek.find(str1) >= 0:
        print("A karakter számjegy.")
    else:
        print("A karakter írásjel.")

    if number % 3 == 0 and number % 5 == 0:
        print("Osztható hárommal és öttel.")
    elif number % 3 == 0:
        print("Csak hárommal osztható.")
    elif number % 5 == 0:
        print("Csak öttel osztható.")
    else:
        print("Nem osztható sem hárommal, sem öttel.")

    grade = random.randint(1, 5)
    if grade == 5:
        print("kiváló")
    elif grade == 4:
        print("jó")
    elif grade == 3:
        print("közepes")
    elif grade == 2:
        print("elégséges")
    elif grade == 1:
        print("elégtelen")
    else:
        print("Nem megfelelő érték.")


except ValueError:
    print("Számot kértem!")