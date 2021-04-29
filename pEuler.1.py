#Eurler project Q.No 1

import math
multilpies = [] #we'll define a list we we'll store all multilpies of 3 and 5 
for i in range(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        multilpies.append(i) # for every number in the range which is a multiply of 3 or 5, we'll add it to the list 
mult_sum = sum(multilpies) # I used the functIon "sum" from the math library, but there's no problem finding the sum without the math libarary
print(mult_sum)
