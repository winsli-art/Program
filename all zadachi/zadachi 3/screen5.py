

def plus(x):
    for i in range(1,len(x)-1):
        if x[i] != '+' and x[i-1] == '+' and x[i+1] == '+':
            return True
        else:
            return False
        

