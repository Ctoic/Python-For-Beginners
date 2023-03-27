# Including numpy in python
import numpy as np 

# adding  a list to another list

list = [2 , 3 ,4 ,4 ,4 ]
list2 = [3 ,4 ,5,5,5,6,]

list3 = list+list2
print("List 3:`",list3)

# adding numpy arrray to list
print("List 4")
list4 = np.array(list3)
print(list4)
print("List 5")
list5 = np.array(list3) + list4

print(list5)


print(len(list4))
print(len(list3))
