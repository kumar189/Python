num=[]
#all numbers in range are checked whether they are divisible by 2&7 or not
for n in range(700,1700):
    if(n%2==0) and(n%7==0):
        num.append(str(n))
print(num)
