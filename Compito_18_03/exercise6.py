parola= input("Scrivi una parola: ")

if len(parola)<=5:
    print("Parola Corta")
elif len(parola)>5 and len(parola)<=8:
    print("Parola Media")
else:
    print("Parola Lunga")