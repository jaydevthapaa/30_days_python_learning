# literals :    raw data given in a variable 
# types :   Numeric, string, boolean, special literals

# Numberic literals

a= 0b1010  #binary literals
b= 100 # decimal literals
c= 0o310  #octal literals
d= 0x12c #hexadeciamal


# float literals

float_1= 10.5
float_2= 1.5e2
float_3= 1.5e-3

# complex literal
x=3.14j

print(a, b, c, d)
print(float_1,float_2,float_3)
print(x, x.imag, x.real)


# string literals
abc='this is 1st type'
abcd="this is 2nd type"

# multiline string
abcde="""this is multline string can be used inside three inveted """
unicode=u"\U0001f600"
raw_string= r"raw \n string"

print(abc)
print(abcd)
print(abcde)
print(unicode)
print(raw_string)

# boolean literals

f= True + 4
g= False + 10

print("a: ", a)
print("b: ", b)

# special literals
a= None
print(a)
