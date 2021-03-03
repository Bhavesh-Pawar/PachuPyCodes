import random as r
a=r.randint(1001,10000)
b=int(input("Enter your choice (4 digit without repeating the digit): "))
bull=0
cow=0
l1=[]
l2=[]
print("Your choice : ",b)
print("Bot's choice : ",a)
while a>0 and b>0:
    temp1=a%10
    temp2=b%10
    l1.append(temp1)
    l2.append(temp2)
    a=a//10
    b=b//10
for i in l1:
    if i in l2:
        cow=cow+1
for i in range(len(l1)):
    if l1[i]==l2[i]:
        bull=bull+1
print(cow)
print(bull)