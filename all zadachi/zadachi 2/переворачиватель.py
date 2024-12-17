



def revers(x):
    result = ''
    b = ''
    for i in range(len(x)-1,-1,-1):
        b = x[i]
        if b == b.upper():
            b = b.lower()
        else:
            b = b.upper()
        result += b
            
    return(result)


print(revers('АлЕкСеЙ'))

