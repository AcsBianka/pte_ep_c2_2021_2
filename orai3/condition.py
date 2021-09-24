number = -20
if number < 100:
    print("Ez a szám kisebb mint 10.")
else:
    print("Ez a szám nagyobb vagy egyenlő mint 10.")


if number > 100:
    print("Ez a szám nagyobb, mint 100.")
else:
    print("Ez a szám nem nagyobb vagy egyenlő mint 100.")


if number%2 == 0:
    print("Ez a szám páros.")
else:
    print("Ez a szám páratlan.")


number2 = 40
if number % number2 == 0:
    print("A ", number2, "osztója a", number)
else:
    if number2 % number == 0:
        print("A ", number, "osztója a", number2, "-nak/nek.")
    else:
        print("Egyik sem osztója a másiknak.")


str1 = "almaszár"
if str1[0] == str1[-1]:
    print("A szöveg első és utolsó karaktere megegyezik.")
else:
    print("A szöveg első és utolsó karaktere nem egyezik meg.")


if number > 0:
    print("Ez a szám pozitív előjelű.")
else:
    if number < 0:
        print("Ez a szám negatív előjelű.")
    else:
        print("Ez a szám nulla.")

#2. megoldás

if number > 0:
    print("Ez a szám pozitív előjelű.")
elif number < 0:
        print("Ez a szám negatív előjelű.")
else:
        print("Ez a szám nulla.")


if str1[0].isupper():
    print("Nagybetűvel kezdődik.")
else:
    print("Nem nagybetűvel kezdődik.")

str2 = "almafa"
if str1[0:5] == str2[0:5]:
    print("Az első 5 karaktere megegyezik")
else:
    print("Nem azonos az első 5 karaktere.")