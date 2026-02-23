age= input("Enter your age: ")
age= int(age) #convert the input to integer
if(age >18):
  print("You are eligible for driving license")
elif(age == 18):
    print("You are eligible for both driving license and vote")
else:    print("You are not eligible for driving license and vote")