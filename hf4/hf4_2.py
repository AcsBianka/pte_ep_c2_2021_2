
a1 = int(input("A sorozat első eleme: "))
a2 = int(input("A sorozat második eleme: "))
n = int(input("Adja meg hányadik elemét szeretné tudni: "))
q = a2/a1
print("Kvóciens:", q)
i = 0
while i <= n:
    an=a1*(q**n-1)
    i=i+1
print("Az n. elem: ", an)