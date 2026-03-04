# questo è un commento
#cosa è una variabile?
# una variabile è un contenitore che memorizza un valore. che può essere di diversi tipi e può cambiare durante l'esecuzione del codice.

#assegno una variabile
mioNome = "Luca" #stringa
miaEta = 18 #intero
corso = "TecnicoInformatico" #stringa
altezza = 1.74 #float (NUMERO CON LA VIRGOLA)

#indipendentemente dal tipo che scelgo non viene dichiarato da nessuna parte. questo comportamento è tipico dei linguaggi debolmente tipizzati

# ESERCIZIO: Istanzia 2 variabili (nome a scelta libera) di tipo intero. con queste 2 variabili elabora le 4 operazioni matematiche (+ - * /) e stampa il risultato di ogni operazione.
numero1 = 100
numero2 = 1.04
somma = numero1 + numero2
differenza = numero1 - numero2
prodotto = numero1 * numero2
quoziente = (round (numero1 / numero2), 2)
print("La somma è: " + str(somma))
print("La differenza è: " + str(differenza))
print("Il prodotto è: " + str(prodotto))
print("Il quoziente è: " + str(quoziente))

#numeri con la virgola: float
pi = 3.14
temperatura = 36.5
#voglio controllare di che tipo sono pi e temperatura
print(type(pi))
print(type(temperatura)) 

calcolo = 0.1 + 0.2
print(calcolo) #il risultato è 0.30000000000000004 Attenti alla precisione
print (round(calcolo, 2)) #dopo la virgola segni quante cifre voglio mostrare

#STRINGHE : sono sequenze immutabili di caratteri. Le stringhe sono il modo umano di comunicare

nomeUser = "Luca"
emailUser = "alibabba@gmail.com"
corso = "TecnicoInformatico"

#concateniamo le stringhe
saluto = "Ciao, mi chiamo " + nomeUser + " e il mio email è " + emailUser + " e frequento il corso " + corso
print(saluto)

print("ti prego fatemi andare a casa, ho fame, ho sonno, mi sto rompendo le palle, voglio vedere il mio episodio di Pokémon Accademy per dio")

mioNome = "Luca"
mioCognome = "Benedetto"
miaEta = 18
mioCorso = "TecnicoInformatico"
print(f"Ciao, mi chiamo {mioNome} {mioCognome} e ho {miaEta} anni, frequento il corso {mioCorso}.")
