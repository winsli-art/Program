


def useless (a):
    n = len(a)
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    
    result = max / n
    return result