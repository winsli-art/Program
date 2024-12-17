def all_eq(lst):
    max = len(lst[0])
    last = ''
    for i in range (1,len(lst)):
        if len(lst[i])> max:
            max = len(lst[i])
    for i in range (0,len(lst)):
        lain = max - len(lst[i])
        for z in range (0,lain):    
            last = last + '_'
        lst[i] = lst[i] + last
    
    
    return(lst)


        