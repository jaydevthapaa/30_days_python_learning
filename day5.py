# operators are used to perform operation on variable and values. Python has following operators:

#   1   :   Arithmetic operators
a=4
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)  #integer divison

#   2   :   comparison operator
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


#   3   : logical operators
x= True
y= False

print(x or y)
print(x and y)
print(not x)
print(not y)

#   4   : bitwise operators useful while working with binary values
d=2
e=3
print(d & e)
print(d|e)
print(d>>2)
print(e<<3)

#   5   : Assignment operator
g=5 # = is assignment operator
g += 3
print(g)

#   5   :identity operator    :   checks wheather the  varibales located in same memory location or not

a= "hello"
b= "hello"

print(a is b)

a = [1,2,3]
b = [1,2,3]
print(a is b)

a="Hello-world"
b="Hello-world"
print(a is b)

#   5: membership operator tells us about wheather inside of any thing or not
x= "bhaktapur"
print("b" in x)
print("b" not in x)

a = [1,2,3]
print(3 in a)




