

def suma_str(x):
    number = ''
    total_sum = 0
    for i in x:
        if i.isdigit():
            number += i
        else:
            if number != '':
                total_sum += int(number)
                number = ''
    if number:
        total_sum += int(number)

    return(total_sum)



print(suma_str('1aasd2312a3'))

