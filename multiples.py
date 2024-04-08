total=0
num1, num2=map(int,input("enter 2 number with space").split())
below=int(input("enter the number under which you want to find multiples"))
print("multiple of",num1,"below 10 are")
for i in range(1,below):
    if i%num1==0:
        print(i)
        total+=i
        
tot=0
print("multiple of",num2,"below 10 are")
for j in range(1,below):
    if j%num2==0:
        print(j)
        tot+=j


print("sum of multiple of",num1,"and",num2,"below",below,"are",total+tot)
