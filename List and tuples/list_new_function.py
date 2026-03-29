#Append function is used to add an element at the end of the list. It takes only one argument which is the element to be added. The syntax for append function is as follows:

list= [3,4,5,6,7,8,9]
list.append(10)
print(list)

#list.sort( )  #sorts in ascending order 

list.sort() #automatically sort the list in ascending order
print(list)
list.sort(reverse=True) #sorts in descending order
print(list)

char=['a','b','c','d','e','g','f']
char.sort()
print(char)
char.sort(reverse=True)
print(char)