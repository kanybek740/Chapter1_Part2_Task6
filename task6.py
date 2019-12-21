#  vyvodit desyati4noe chislo

num = int(input())
p = (num % 100)//10
print(p)
 
# vyvodit desyatoe chislo po s4etu

num = input('vyvedet desyatoe chislo: ')
b = num * 10
print(b[9])

#  3-yi variant
chet = 1 
for i in range(11):
    for n in num:
        if chet == 10:
            print(n)
            break
        else:    
            chet = chet + 1
        chet == 10
    print(n)
    break