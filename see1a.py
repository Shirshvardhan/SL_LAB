print("ENTER THE INTEGER INPUTS: ")
a=input().split()
arr=[int(i) for i in a]
print("MIN",min(arr))
print("MAX",max(arr))

print("ENTER AN ELEMENT TO BE INSERTED INTO THE LIST: ")
i= int(input())
arr.append(i)
print(arr)

print("ENTER AN ELEMENT TO BE DELETED FROM THE LIST: ")
i= int(input())
arr.remove(i)
print(arr)

print("ENTER AN ELEMENT TO BE SEARCHED FROM THE LIST: ")
i= int(input())
if(i in arr):
	print("PRESENT")
else:
	print("NOT PRESENT")

