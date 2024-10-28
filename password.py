'''creattion of a Random password generator program
 Author: S Hithesh Reddy'''
import string
import random
print("***Welcome***")
length=int(input("Enter the length of your password: "))
print("We have two levels of security in our generated passwords.")
print("1.without special characters(low security)")
print("2.with special characters(high security)")
choice=int(input("Enter your choice: "))
total_characters=string.ascii_letters + string.digits
password=""
if(choice==1):
    for i in range(length):
        password+=random.choice(total_characters)
elif(choice==2):
    total_characters+="@!#$%&*_"
    for i in range(length):
        password+=random.choice(total_characters)
else:
    print("check your choice again.")
    exit
print("The Generated password is: "+password)
print("***Thank you***")
