from functools import reduce
a = [1,24,7,42,27,9]
print("THE FIRST LIST(a) IS\n",a)
b = [i*3 for i in a]
print("THE TRIPLE MULTIPLIED LIST(b) IS\n",b)

sum1 = reduce((lambda x,y:x+y),a)
print("SUM OF LIST a is:\t",sum1)

sum2 = reduce((lambda x,y:x+y),b)
print("SUM OF LIST b is:\t",sum2)

