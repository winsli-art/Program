

def blackjack(x):
    suma = 0
    for i in range(len(x)):
        suma += x[i]
    if suma > 21:
        print(True)
    else:
        print(False)
