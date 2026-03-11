# IF STATEMENT. Questo costrutto serve a controllare e prendere una scelta
# Operatori di confronto
#== (uguale a)
#!= (diverso da)
#> (maggiore di)
#< (minore di)
#>= (maggiore o uguale a)
#<= (minore o uguale a)

#Tutte le volte uso un operatore di confronto sto generando un valore booleano (True o False)

#I valori booleani mi servono negli If statement

#SINTASSI:
# if condizione:
#     corpo dell'if che viene eseguito se la condizione è true
# else:
#     corpo dell'else che viene eseguito se la condizione è false

#Esempio:
piove = False

if piove:
    print("porto l'ombrello")
else:
    print("non porto l'ombrello")

#Altro esempio:
miaEta = 18

if miaEta >= 18:
    print(f"Io ho {miaEta} anni e sono maggiorenne")
elif miaEta < 0:
    print("Coglione metti un'età valida")
else:
    print(f"Io ho {miaEta} anni e sono minorenne")

#Altro esempio ancora:
etaLorenzo= 18
etaSanna = 17

if etaLorenzo > etaSanna:
    print("Lorenzo è più grande di Sanna")
elif etaLorenzo == etaSanna:
    print("Lorenzo e Sanna hanno la stessa età")
else:
    print("Sanna è più grande di Lorenzo")

# Ennesimo esempio in più: confronto tra stringhe
parola1 = "Ciao"
parola2 = "Ciao"
parola3 = "CiaO"

if parola1 == parola2:
    print("Le parole sono uguali")
elif parola1 != parola3:
    print("Le parole sono diverse")
else:
    print("non mi hai fornito le due parole")

#Esempio 5 confronto tra stringhe senza tener conto di uppercase e lowercase

stringa1 = "Caffè"
stringa2 = "caffè"

if stringa1.lower() == stringa2.lower():
    print(f"Le stringhe sono uguali: {stringa1}")
else:
    print(f"Le stringhe sono diverse: {stringa1} e {stringa2}")

#Esempio 6 - Altri confronti tra stringhe
#Possiamo creare porzioni di stringhe
frase= "Ciao Luca, come stai?"

print(frase.startswith("Cia")) #True
print(frase.endswith("?")) #True
print("Luca" in frase) #True
if "Luca" in frase:
    print("Luca è presente nella frase")
else:
    print("Luca non è presente nella frase")

if frase.startswith("Cia"):
    print("La frase inizia con 'Cia'")
else:
    print("La frase non inizia con 'Cia'")

#Esempio 7 - Voto e valutazione
# Patente di Guida. per iscrivermi all'esame devo aver compiuto 18 anni

etaStudente = int(input("Quanti anni hai? "))
nomeStudente = input("Come ti chiami? ")
if etaStudente >= 18:
    print(f"Benvenuto {nomeStudente}, puoi iscriverti all'esame della patente")
elif etaStudente < 18 and etaStudente > 15:
    print(f"Benvenuto {nomeStudente}, con la tua età puoi iscriverti alla patente AM")
else:
    print(f"Mi dispiace {nomeStudente}, non puoi iscriverti alla patente")