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



#list.reverse( )  #reverses list 
number=[1,2,3,4,6,8,9]
number.reverse()
print(number)


#list.insert( idx, el )  #insert element at index 
num=[1,3,5,7,9]
num.insert(1,4)
print(num)


#list.remove(1)  #removes first occurrence of element
num.remove(5)
print(num)


#list.pop( idx )  #removes element at idx 
num.pop(2) #removes element at index 2
print(num)
