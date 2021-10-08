text = str(input("Kérem adjon meg egy szöveget: "))
r_text = text[::-1]
for i in range(len(text)):
    if text[i] == r_text[i]:
        print("A szöveg palindrom")
    else:
        print("Nem palindrom")


