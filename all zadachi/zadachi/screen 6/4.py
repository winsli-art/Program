
dict = {1:1,3:3,2:2,5:5,4:4}


def dicter(x):
    keys = list(x.keys())
    print(keys)
    x[keys[0]], x[keys[-1]] = x[keys[-1]], x[keys[0]]
    del x[keys[1]]
    x['new key'] = 'new value'
    return x
print (dicter(dict))

