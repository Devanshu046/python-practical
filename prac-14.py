# Python program to swap element of a list

# Getting list from user
myList = []
length = int(input("Enter number of elements: "))
for i in range(0, length):
    val = int(input("enter number:"))
    myList.append(val)

print("Enter indexes to be swapped ")
index1 = int(input("index 1: "))
index2 = int(input("index 2: "))

print("Initial List: ", myList)
# Swapping given elements
myList[index1], myList[index2] = myList[index2], myList[index1]

# Printing list 
print("List after Swapping: ", myList)
