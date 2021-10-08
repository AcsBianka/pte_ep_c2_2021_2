filepath = "lorem.py"
fileobject = open(filepath, "r+")
print(fileobject.read())
fileobject.close()