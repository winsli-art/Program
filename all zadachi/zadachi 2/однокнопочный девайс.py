a = [0,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
b = [0]
message = input()
kol = 0
for i in message:
    b.append(i)
for x in range (0,len(b)):
    for i in range(0,len(a)):
        if a[i] == b[x]:
            kol = kol + i
kol = str(kol)
print("кнопок:"+ kol)

    
