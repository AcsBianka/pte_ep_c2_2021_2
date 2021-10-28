filepath = "fajl1.txt"
fileobject = open(filepath, "r")
count_rows, count_character = 0,0
for line in fileobject:
    count_rows += 1
    count_character += len(line)
count_character -= count_rows
print("A sorok száma: ", count_rows,"db A karakterek száma: ",count_character)