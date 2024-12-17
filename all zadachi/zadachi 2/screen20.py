




def vosr(x):
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            result = 1
        else:
            result = 0
    if result == 1:
        print('возростает')
    if result == 0:
        print('не возростает')

vosr([1,2,4,3])