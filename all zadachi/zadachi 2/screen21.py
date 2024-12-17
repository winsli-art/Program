



def mediana(x):
    if len(x) % 2 == 0:
        chet = 0
    else:
        chet = 1

    if chet == 1:
        i = len(x) // 2
        return(x[i])
    if chet == 0:
        i = len(x)/2
        result = (x[i] +x[i+1])/2
        return(result) 
    

print(mediana([1,2,3,4,6]))
