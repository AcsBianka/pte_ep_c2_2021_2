szoveg = input("adjon meg egy szöveget: ")
hossz = len(szoveg)
#print(hossz)
tomb = []
for i in range(hossz):
    tomb.append(szoveg[i])
for i in range(hossz):
    if(tomb[i] != " "):
        if(tomb[i].islower() == True):
            tomb[i] = tomb[i].upper()
        else:
            tomb[i] = tomb[i].lower()
kiiras = ""
for char in tomb:
    kiiras = kiiras + char
print(kiiras)
