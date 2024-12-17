

def list_sort(lst):
    y = len(lst)
    for i in range(y):
        for j in range(0, y-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] =  lst[j+1],lst[j]
    return(lst)