




def enemy(x):
    result=[]
    b = ['Артём','Алексей',"Филипп"]
    for i in x:
        if i not in b:
            result.append(i)

    return(result)
    







print(enemy(['Маша','Артём',"Филипп",'Лиза',"Алексей"]))