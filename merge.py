print("amicables pair upto 10000 are-")
for i in range(2,10000):
    s1=0
    s2=0
    for j in range(1,int((i/2))):
        if i%j==0:
            s1=s1+j
    for k in range(1,int((s1/2))):
        if s1%k==0:

            s2=s2+k
    if s1>i:
        continue
    if s2==i:
        print(i,"&",s1,"\n")
