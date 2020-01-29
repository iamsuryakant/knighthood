a=[10,7,11]
b=[10,9,7,13]
x=[]
for i in a:
    for j in b:
        if i!=j:
            x.append([i,j])
for i in range(len(x)):
    for j in range(2):
        print(x[i][j],"\t",end="")
    print("\n")
