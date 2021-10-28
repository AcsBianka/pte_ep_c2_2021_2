filepath = "szorzotabla.txt"
fileobject = open(filepath, "a")
line = ""
for i in range(10):
    print("\n")
    line = "\n"
    fileobject.write(line)
    file=""
    for j in range(10):
        line += str((i+1)* (j+1))
        line += " "
    fileobject.write(line)