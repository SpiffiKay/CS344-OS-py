###########################################################################
#Title: Program Py
#Name: Tiffani Auer
#Due: Feb 28, 2019
#note: written to be run on Python3 :)
###########################################################################
import random
import string

#generate random string
#adapted from tutorial on https://pynative.com/python-generate-random-string/
def myString(strLength=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(strLength))

#create strings
str1 = myString();
str2 = myString();
str3 = myString();

#print strings to screen
print(str1)
print(str2)
print(str3)

#add newline
str1+='\n'
str2+='\n'
str3+='\n'

#create files
file1 = open("file1", "w+")
file2 = open("file2", "w+")
file3 = open("file3", "w+")

#write string to files
file1.write(str1)
file2.write(str2)
file3.write(str3)

#close files
file1.close()
file2.close()
file3.close()

#generate random numbers
num1 = random.randint(1, 42)
num2 = random.randint(1, 42)

#multiply numbers
total = num1 * num2

#print numbers
print(num1)
print(num2)
print(total)
