#AND Logico: questo mi permette di unire più condizioni creandone una più grande
etaStud = 18
esameTeorico = True

if etaStud >= 18 and esameTeorico:
    print("Puoi fare l'esame pratico")
elif etaStud < 18 and esameTeorico:
    print("Non puoi fare l'esame pratico, devi aspettare di compiere 18 anni")
elif etaStud >= 18 and not esameTeorico:
    print("Non puoi fare l'esame pratico, devi prima superare l'esame teorico")
else:
    print("Non puoi fare l'esame pratico, devi prima superare l'esame teorico e aspettare di compiere 18 anni")