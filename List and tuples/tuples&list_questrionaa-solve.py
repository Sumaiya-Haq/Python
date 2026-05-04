# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.


movie = []
mov1= input("Enter your 1st movie name= ")
mov2= input("Enter your 2nd movie name= ")
mov3= input("Enter your 3rd movie name= ")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print("Your favorite movies are: ", movie)




#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list = [1,2,3]
list2 = [1,2,3]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrom")
else:
    print("not palindrom")



    #WAP to count the number of students with the “A” grade in the following tuple.
grade = ("A", "B", "C", "D", "D", "A", "B")
print(grade.count("A"))


#Store the above values in a list & sort them from “A” to “D”.

grade = ["A", "B", "C", "D", "D", "A", "B"]
grade.sort()
print(grade)

