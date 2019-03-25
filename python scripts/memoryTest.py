import os
import psutil
from time import sleep
from pympler import asizeof
import copy 
import sys
import matplotlib.pyplot as plt
import numpy as np


def copyOnModify(listName,index,value):
	if index == 0:
		listName[index]=copy.deepcopy(listName[index+1])
	else:
		listName[index]=copy.deepcopy(listName[index-1])
	listName[index].age=value


class MyClass:

	classDescription="About Self"
	age=20
  	def __init__(self, fname, lname):
  		self.firstname = fname
  		self.lastname = lname


  	def printname(self):
  		print(self.firstname, self.lastname)

a1=MyClass("A","B")
deep=[copy.deepcopy(a1)]
shallow=[a1]
deepSize=[]
shalSize=[]

print("Making both Deep Copies and Shallow Copies one by one")
print("Deep","Shallow")
# Creating Copies
for j in range(10):
	sleep(0.1)
	deep.append(copy.deepcopy(deep[j])) # making deepCopies of objects from class MyClass
	shallow.append(shallow[j]) # making shallowCopies of objects from class MyClass
	print(j,asizeof.asizeof(deep),j,asizeof.asizeof(shallow))
	deepSize.append(asizeof.asizeof(deep))
	shalSize.append(asizeof.asizeof(shallow))

print("\nArray of Deep Copies\n")	
print("array created",deep)
print("\nArray of Shallow Copies\n")	
print("array created",shallow)
print("\n")

#using this to check on the method. Modifying the object in the index '2' in the list 'shallow'
#copyOnModify(shallow,2,30)


print("Deleting both Deep Copies and Shallow Copies one by one")
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


t = np.arange(0.0, 2.0, 0.01)

s1 = deepSize
s2 = shalSize

fig, axs = plt.subplots(1, 1, sharex=True)
axs.set_ylabel("Bytes")
axs.set_xlabel("Number of copies")
axs.plot(s1,'b.')
axs.plot(s2,'r.')
plt.show()