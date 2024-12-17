


def probel(x):
    result = ''
    i_pred = ''
    result_kon = ''
    for i in x:
        if i  != ' ' or i_pred != ' ':
            result += i
        i_pred = i  
    for j in range(1,len(result)):
        result_kon += result[j]

    
    
    return(result_kon)
    




    

print(probel('     лёша      навальный      '))