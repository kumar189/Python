#imports numpy
import numpy as np
#creates a random integers of size15 with in range of 1 to 15
k=np.random.randint(1,15,15)
#prints all random integers
print (k)
#max function returns the maximum value in a
y=k.max()
#prints maximum value
print(y)
#checks for maximum value in a and replaces with 100
for i in range(14):
    if(k[i]==y):
        k[i]=100
#prints a where maximum values are replaced with 100
print(k)