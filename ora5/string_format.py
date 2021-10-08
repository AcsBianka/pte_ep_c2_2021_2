number = 5
number2 = number * 2
print("A number változó értéke ", number, ". Ha megszorzom kettővel, akkor ", number2, "-t kapok.")
print("A number változó értéke ", number, ". Ha megszorzom kettővel, akkor ", number2, "-t kapok.", sep="")
print(f"A number változó értéke: {number}. Ha megszorzom kettővel, akkor {number2} -t kapok.")
print("A number változó értéke {}. Ha megszorzom kettővel, akkor {} -t kapok.".format(number, number2))

#igazítások
print(f"A number változó értéke: {number:<3}. Ha megszorzom kettővel, akkor {number2:>5} -t kapok.")
print("A number változó értéke {:^6}. Ha megszorzom kettővel, akkor {:^6} -t kapok.".format(number, number2))

#számformátumok

number = 125
print(f"A szám bináris alakja: {number:b}, az oktális alakja: {number:o}, a decimális alakja: {number:d}, a hexadecimális alakja: {number:x} és {number:X}")
print("A szám bináris alakja: {:b}, az oktális alakja: {:o}, a decimális alakja: {:d}, a hexadecimális alakja: {:x} és {:X}".format(number, number, number, number, number))

number = 65
print(f"{number:c}")
print("{:c}".format(number))

number = 100.12345
print(f"Tudományos: {number:e} vagy {number:E}")
print(f"3 tizedesjegy pontosság: {number:.3f}")
print(f"15 karakteren: {number:15f}")
print(f"15 karakteren: {number:15%}")