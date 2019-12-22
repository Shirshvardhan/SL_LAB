atomic = {"H":"hydrogen","He":"helium","Li":"lithium","O":"oxygen"}
print(atomic)
sym = input("ENTER AN EXISTING SYMBOL: ")
name = input("ENTER AN ELEMENT NAME: ")
atomic[sym] = name
print(atomic)
sym = input("ENTER AN NEW SYMBOL: ")
name = input("ENTER A NEW ELEMENT NAME: ")
atomic[sym] = name
print(atomic)

flag  = 0
ele=input("ENTER AN ELEMENT TO SEARCH: ")
for i in atomic:
	if(i == ele):
		print("ELEMENT FOUND")	
		flag = 1
if(flag ==0):
	print("ELEMENT NOT FOUND")	