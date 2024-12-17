


import math
def pifagor(x):
    xa, ya = x['xa'],x['ya']
    xb,yb = x['xb'], x['yb']
    result = math.sqrt((xa - xb)**2 + (ya - yb)**2)
    return(result)





print(pifagor({'xa' :0,'ya': 0,'xb':4,'yb':3 }))