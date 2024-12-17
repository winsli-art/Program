


def corob(x):
    result = 0
    for i in range(0,len(x),3):
        V = x[i] * x[i+1] * x[i+2]
        result += V
    return(result)
    



