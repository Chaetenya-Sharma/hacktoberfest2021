# Python program to find largest
# number in a list
  
# list of numbers
lst = []
 
# number of elements as input
n = int(input("Enter number of elements:"))
print("Give values in list:")
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
  
# sorting the list
lst.sort()
  
# printing the last element
print("Largest element is:", lst[-1])
