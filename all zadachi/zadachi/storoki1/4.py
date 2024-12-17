



def camel(st):
    result = ''
    if st[0] == st[0].lower():
        x = 0
    else:
        x = 1
    for i in st:
        if i != ' ':
            if x == 0:
                result += i.upper()
                x = 1
                
            elif x == 1:
                result += i.lower()
                x = 0
        else: 
            result += i

    return result


print(camel('Филип лох'))



