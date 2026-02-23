age= input("Enter your age: ")
age= int(age) #convert the input to integer
if(age >18):
  print("You are eligible for driving license")
elif(age == 18):
    print("You are eligible for both driving license and vote")
else:    print("You are not eligible for driving license and vote")


#NESTING IF STATEMENT
age= 99
if(age > 18):
    if(age>=90):
        print("You are too old to drive")
    else:
        print("You are eligible for driving license")
else:
    print("You are not eligible for driving license")


    #WAP to check if a number entered by the user is odd or even.
number= int(input("Enter a number: "))
if(number%2==0):
    print("The number is even")
else:
    print("The number is odd")
  

  #WAP to find the greatest of 3 numbers entered by the user.
