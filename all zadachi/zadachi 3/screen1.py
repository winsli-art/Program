

def play(x,y):
    x = x.lower()
    y = y.lower()
    k = 'камень'
    n = 'ножницы'
    b = 'бумага'
    if x == y:
        print('ничья')
    if x == k and  y == n:
        print('первый выиграл')
    if x == n and y == b:
        print('первый выиграл')
    if x == b and y == n:
        print('первый выиграл')


    if x == k and y == b:
        print('второй выиграл')
    if x == n and y == k:
        print('второй выиграл')
    if x == b and y == n:
        print('второй выиграл')

        
