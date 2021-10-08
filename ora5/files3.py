fileobject1 = open("fajl1.txt", "r")
fileobject2 = open("fajl2.txt", "r")
merged_fileobject = open("merged_files", "w")
line1 = fileobject1.readline()
line2 = fileobject2.readline()
while line1 !="" or line2 != "":
    merged_fileobject.write(line1)
    merged_fileobject.write(line2)
    line1 = fileobject1.readline()
    line2 = fileobject2.readline()

fileobject1.close()
fileobject2.close()
merged_fileobject.close()
