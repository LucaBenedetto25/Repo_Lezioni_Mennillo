nome=input("Inserisci il tuo nome:")
eta=int(input("Inserisci la tua età:"))

if eta <= 0 or eta >= 120:
    print("Età non valida")
else:
    print(f"Allora, {nome} tra 5 anni avrai {eta + 5} anni")
    