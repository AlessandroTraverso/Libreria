from GestioneNomi import VisualizzaNome


def funzione():
    print("Sono una funzione che funziona funzionalmente alla tua richiesta caro utente")

def funzione2(nome):
    print("Ciao ",nome,"!")

funzione()
print("Inserire nome:")
x = input()
y=3
funzione2(x)
funzione2(y)
VisualizzaNome("Luca")