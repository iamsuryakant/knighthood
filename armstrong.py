a=int(input("enter the numbers"))
sum=0
temp=a
while temp!=0:
    i=temp%10
    sum=sum+i*i*i
    temp=temp//10
if (a==sum):
    print("armstrong number")
else:
    print("non armstrong number")