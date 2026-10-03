# break
for i in range(1,11):
    if i==5:
        break
    print(i)

# continue
for i in range(1,11):
    if i==5:
        continue
    print(i)
    print("hi")

# pass
for i in range(1,2):
    pass  


# build in functions in python
# 1.print
print("hello world")

# 2.input
name= input("enter your name : ")
print("you entered your name is: ",name)

# 3.type
a=5
print("the type of a is: ", type(a))

# 4.int
b=int('3')
c=int(5.6)
print("the value of b after converting string to int is: ",b)
print("the value of c after converting float to int is :", c)

# 5.abs
d=6.5
print("the abs value of d 6.5 is: ", abs(d))

# 6. pow
print("The pow value of 2,4 after implemenating is : ",pow(2,4))

# 7. min/max
print("the minimum value form the given list is : ",min([4,5,3,1,6,87,7]))
print("the maximum value form the given list is : ", max([4,5,3,1,6,87,7]))

# 8. round
print("The round value of 22/7 is",round(22/7))

# 9. divmod
print("the divmod value of 5,2 is : ",divmod(5,2))

# 10. bin/oct/hex
print("the binary value of 4 is : ",bin(4))
print("the octal value of 4 is : ",oct(4))
print("the hexadecimal value of 3 is : ", hex(3))

# 11. id
a=3
print("the id of a stored in memory location is :",id(a))

# 12. ord
print("the asce code of A is : ",ord('A'))

# 13. len
print("the length of bhaktapur is : ", len("bhaktapur"))

#14. sum
print("the sum of list is : ",sum([1,2,3,4,5]))

# 15. help
print("the help for sum is : ",help('sum'))