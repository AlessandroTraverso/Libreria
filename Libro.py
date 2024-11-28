def AggiuntaLibro(lista):
    print("Quanti libri vuoi inserire all'interno della libreria?")
    x = int(input())
    for i in range (x):
        print("Inserisci il titolo del libro numero" ,i+1)
        titolo = input()
        titolo = titolo.lower()
        lista.append(titolo)
        print("Il libro dal titolo " + titolo + " è stato inserito nella libreria")
    lista.sort()
    print("Questa è la tua libreria in ordine alfabetico:")
    print(lista)



def PrestitoLibro(lista,prestati):
    print("Quanti libri vuoi prendere in prestito?")
    x = int(input())
    while(x>len(lista)):
        print("Non puoi prendere ",x," libri in prestito, ce ne sono solo ",len(lista)," nella libreria")
        print("Reinserisci quanti libri vuoi prendere in prestito")
        x = int(input())
        print("Questi sono i libri disponibili per il prestito nella libreria")
        print(lista)
    for i in range(x):
        print("Inserisci il titolo del libro numero" ,i+1, "che vuoi prendere in prestito")
        titolo = input()
        titolo = titolo.lower()
        if titolo in lista:
            prestati.append(titolo)
            lista.remove(titolo)
            print("Il libro dal titolo " + titolo + " è stato prestato e quindi rimosso dalla libreria")
        elif(titolo in prestati):
            print(f"Purtroppo il libro " + titolo + " è al momento in prestito")
        else:
            print(f"Purtroppo il libro " + titolo + " non è disponibile")
    lista.sort()
    prestati.sort()



def RestituzioneLibro(lista,prestati):
    print("Quanti libri vuoi restituire?")
    x = int(input())
    y = len(prestati)
    for i in range (x):
        print("Inserisci il titolo del libro numero" ,i+1, "che vuoi restituire")
        titolo = input()
        titolo = titolo.lower()
        if titolo in prestati:
            prestati.remove(titolo)
            lista.append(titolo)
            print("Perfetto, Il libro dal titolo " + titolo + " è stato reinserito nella libreria")
        else:
            print("Il libro dal titolo " + titolo + " non risulta prestato")
    lista.sort()
    prestati.sort()



def DispLibro(lista,prestati):
    print("Di quanti libri vuoi verificare la disponibilità?")
    x = int(input())
    for i in range (x):
        print("Inserisci il titolo del libro numero" ,i+1, "di cui vuoi verificare la disponibilità")
        titolo = input()
        titolo = titolo.lower()
        if titolo in lista:
            print("il libro dal titolo " + titolo + " è disponibile nella libreria")
        elif titolo in prestati:
            print("il libro dal titolo " + titolo + " è attualmente in prestito")
        else:
            print("il libro dal titolo " + titolo + " non è nella libreria e non è prestato")



def DispLibreria(lista):
    print("Libri attualmente nella libreria:")
    print(lista)



def LibriPrestati(prestati):
    print("Libri attualmente in prestito:")
    print(prestati)