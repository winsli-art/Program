

def two(x):
    a = []
    for i in x:

        a.append(i)
    for j in range(0,len(a)-1):
        if a[j]== a[j+1]:
            return(True)
        

print(two('абсв'))
