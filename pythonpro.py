print("hello");
a=30
b=40
c=a+b
print (c);
a=9
b=7
c=a*b
print(c);
#even or odd
num=int(input("enter a number:"))
if (num % 2 ==0):
    print("even number")
else:   
    print("odd number") 
#largest of 3numbers
a=int(input("enter a first number")) 
b=int(input("enter a second number"))
c=int(input("enter a third number"))
if(a>b) and (a>c):
    print("largest is:",a)
elif(a>b):
    print("largest number is:",b)
else:
    print("largest number is:",c)  
#factorial
num=int(input("enter the number"))
fact=1
for i in range(1,num+1): 
    fact = fact*i
print("factorial=",fact)     