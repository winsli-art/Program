

def znak(x):
    result = ''
    i_pred = ''
    if x.find('!') == True:
        for i in x:
            if i != '!' or i_pred !='!':
                result += i
            i_pred = i
    else:
        i_pred =''
        for i in x:
            if i != '?' or i_pred !='?':
                result += i
            i_pred = i
    
    
    return(result)

print(znak("филипп???"))
