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

number1= int(input("Enter 1st number: "))
number2= int(input("Enter 2nd number: ")) 
number3= int(input("Enter 3rd number: "))
if(number1>number2 and number1>number3):
    print("The greatest number is", number1)
elif(number2>number1 and number2>number3):
    print("The greatest number is", number2)
else:
    print("The greatest number is", number3)

  
  #WAP to check if a number is a multiple of 7 or not.
  
number= int(input("Enter a number: "))
if(number%7==0):
    print("The number is a multiple of 7")
else:  
    print("The number is not a multiple of 7")