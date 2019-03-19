import os
import psutil
from time import sleep
from pympler import asizeof
import copy 
import sys

def copyOnModify(listName,index,value):
	if index == 0:
		listName[index]=copy.deepcopy(listName[index+1])
	else:
		listName[index]=copy.deepcopy(listName[index-1])
	listName[index].a=value


class MyClass:
  a = "A Class"

a1=MyClass()
deep=[copy.deepcopy(a1)]
shallow=[a1]

print("Deep","Shallow")
# Creating Copies
for j in range(10):
	sleep(0.1)
	deep.append(copy.deepcopy(deep[j])) # making deepCopies of objects from class MyClass
	shallow.append(shallow[j]) # making shallowCopies of objects from class MyClass
	print(j,asizeof.asizeof(deep),j,asizeof.asizeof(shallow))

print("\nArray of Deep Copies\n")	
print("array created",deep)
print("\nArray of Shallow Copies\n")	
print("array created",shallow)
print("\n")

#using this to check on the method. Modifying the object in the index '2' in the list 'shallow'
#copyOnModify(shallow,2,"Modifying this") 


print("Deep","Shallow")
# Releasing Reference
for i in range(len(deep)-1,0,-1):
	sleep(0.2)
	del deep[i]
	del shallow[i] 
	print(i-1,asizeof.asizeof(deep),i-1,asizeof.asizeof(shallow))

print("\nArray of Deep Copies\n")	
print("array deleated",deep)
print("\nArray of Shallow Copies\n")	
print("array deleted",shallow)

