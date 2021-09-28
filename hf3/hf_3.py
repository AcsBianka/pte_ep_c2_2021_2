
input_gender = input("Adja meg a nemét (m-fiú, f-lány):")

if input_gender == "m":
    print("Sajnos nem játszhat a csapatban.")
else:
    input_age = input("Adja meg az életkorát:")
    int_input_age = int(input_age)
    if 12 > int_input_age > 10:
        print("Játszat a csapatban!")
    else:
        print("Sajnos nem játszhat a csapatban.")

