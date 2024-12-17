


def mul_to_int(a,b):
    result = a*b
    if int(result) == result:
        return(int(result))
    else:
        return(float(result))
    

print(mul_to_int(2,6))   