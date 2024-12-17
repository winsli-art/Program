


def change(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]
    return(lst)

print(change([1,5,4,6]))