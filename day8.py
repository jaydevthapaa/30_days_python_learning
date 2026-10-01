# range is a build in module in py

print(range(1,11))
print(list(range(1,11)))
print(list(range(11)))
print(list(range(1,11,2)))
print(list(range(11,0,-1)))

# sequence is order can be sting, list, tuple.....
print("bhaktapur")


for i in range(1,11):
    print(i)

for i in range(11,0,-1):
    print(i) 
    
for i in "kathmandu":
    print(i)

for i in [1,2,3,4,5,6]:
    print(i)

for i in (1,2,3,4,5,6):
    print(i)
    
for i in {1,2,3,4,5,6}:
    print(i)
    
    
    
# nested loop 
rows=int(input("enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(0,i):
        print("$", end=" ")
    print("")