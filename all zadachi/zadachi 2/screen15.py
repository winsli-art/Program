



def umnog(x):
    a = []
    result = 1
    for i in range(0,len(x),2):
        
        y = float(x[i])
        result = result * y
        
    return(result)



print(umnog('3,3'))