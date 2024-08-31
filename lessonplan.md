# Lesson plan
  
**Type Casting**

Converting from one data type to another
Creates a copy of the value.  Does not overwrite the original unless you reassign it over the original variable.
Simply put the data type name followed by the value you want to convert in brackets

E.g.

num = 42
strNum = str(num) #converts to a string

conversion of types so far

str()
int()
float()
bool()

Always works:
int -> str
bool -> str
float -> str
int -> float

bool -> int
bool -> float
False becomes 0 or 0.0
True becomes 1 or 1.0

float -> int
removes values after decimal points (rounds down)

str -> bool
int -> bool
float -> bool
0 or empty string create False. anything else creates True

Sometimes works: (input must be compatible)
str -> int
str -> float

Examples Lesson:


'''
Lesson 1.5 - Type casting(converting) and documentation
Author: Mr. Kalisz
Date Created: September 22, 2020
Date Last Modified: September 22, 2020
'''

#Typecasting (Converting data to other types)

#can not go from a more complicated type to a simpler type
#These are called non-primitive and primitive types respectively

#Primitive types we know so far - int, float

#Non-primitive types we know so far - String

#Primitive types are data that can not be broken down into smaller types

#Strings can be broken down into characters.  This is why they are not primitive


#Examples

num = 42
strNum = str(num) #Converts to a string ("42")
print("The answer to everything in the universe is " + strNum) #This allows us to concatenate the value to another string
floatNum = float(num) #converts to a float (42.0)
print(floatNum)

print(float(False)) #Outputs zero

floatNum = 45.9
intNum = int(floatNum)#Rounds the number down by getting rid of the decimal point
print(intNum)
print(floatNum) #Typecasting does NOT change the original value.  floatNum is still 45.9, you must assign the value to another variable if you want to keep it

print("Repeat what I did before " + str(num))
print("convert the float to " + str(floatNum))

#print(int("hello")) #Type casiting only works if the value is valid, otherwise it will throw an error.
print(int("10"))