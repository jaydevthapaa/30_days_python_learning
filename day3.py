# user input and type conversion

input("please enter your name: ")

# addition 
# note input always takes input as string format

first_number= input("enter first number: ")
print("the first number you enter is:", first_number)
second_number= input("enter second number: ")
print("the second number you enter is:", second_number)
result= first_number + second_number
print(result)

# since input always takes input as string format it always concatinate the input falues instead of doing addition
# so there comes a solution for this non as type conversion
# type conversion means chanaging  a data type i.e string-> integer, integer->float...... etc
#  two types of type conversion i.e implicit, explicit

# implicit  :   python automatically does type conversion we do not have to define it
# explicit  :   here we define where to convert data types

# example of implicit

print(4+5)
print(5+5+5j)



first_number= int(input("enter first number: "))
print("the first number you enter is:", first_number)
second_number= int(input("enter second number: "))
print("the second number you enter is:", second_number)
result= first_number + second_number
print(result)

# type conversion is not a parmanant operation
