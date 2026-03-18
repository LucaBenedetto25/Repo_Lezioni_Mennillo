#instanziamo delle variabili e poi scriviamo la presentazione tramite print e f-string
nome = "Luca"
cognome = "Benedetto"
eta = 18
corso = "Tecnico Informatico"
altezza = 1.74
presenza = True

print(f"Piacere, \nMi chiamo {nome} {cognome}, ho {eta} anni e sono alto {altezza}.")
print(f"Frequento il corso di {corso}.")

if presenza:
    print("Oggi sono presente.")
else:
    print("Oggi sono assente")

print ("===== IL MIO AMICO =====")
#Adesso presenta un tuo compagno di classe, fai attenzione ad assegnare delle variabili con un altro nome
nomeAmico = "Alessandro"
cognomeAmico = "Marsala"
etaAmico = 17
altezzaAmico = 1.75
presenzaAmico = False
print(f"Lui invece è {nomeAmico} {cognomeAmico},\n ha {etaAmico} anni ed è alto {altezzaAmico}.")

if presenzaAmico:
    print("Oggi è presente.")
else:
    print("Oggi è assente.")

if etaAmico<60:
    print(f"{nomeAmico} è giovane.")
else:
    print(f"{nomeAmico} è un vecchiodemmedda.")