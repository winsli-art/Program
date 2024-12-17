def ticket(x):
    x = x/2
    x = int(x)
    suma = 0
    sum_i = 0
    sum_j = 0
    for i in range (0,10**x):
        for j in range (0,10**x):
            i = str (i)
            j = str (j)
            for num in i:
                sum_i += int(num)
            for num in j:
                sum_j += int(num)
            if sum_j == sum_i:
                suma += 1
            sum_i = 0
            sum_j = 0

    return suma

print(ticket(2))