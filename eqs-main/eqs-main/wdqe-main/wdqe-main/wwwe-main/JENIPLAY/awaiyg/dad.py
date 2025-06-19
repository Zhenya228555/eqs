a = input("ведіть слово:")
palindrom=""
for letter in a:
    palindrom = letter + palindrom
    print(palindrom)
if a == palindrom:
    print("Це полендром")
else: 
    print("Це не поледром")