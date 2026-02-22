str ="I am studing BCSE at IUBAT University"
print(str.endswith("sity")) #True
print(str[0:37])
print(str.endswith("t")) #False

#using capatilize functon

str ="most beautiful hearted person in the world"
print(str)
print(str.capitalize()) #only first letter of the string will be capitalized
str= print(str.capitalize())

#using replace function

str="in future i want to be a AI Engineer"
print(str.replace("I","e")) #replace all the I with e
print(str.replace("AI","ML")) #replace AI with ML

#usig find function

str= "I am a student of BCSE at IUBAT University"
print(str.find("IUBAT")) #find the index of the first character of the word IUBAT


#using count function

str= "I want to be a AI Engineer in future"
print(str.count("a")) #count the number of a in the string


#write a program to input user’s first name & print its length.
name= input("Enter your name:")
print("The length of your name is:",len(name))
print("The length of your first name is:",len(name.split()[0])) #split the name and count the length of the first name
print("The lenght of your last name is: ",len(name.split()[1])) #split the name and count the length of the last name

#WAP to find the occurrence of ‘$’ in a String.
str= " I have $50 in my bank account and I want to buy a new phone that costs $300"
print(str.count("$"))