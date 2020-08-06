a=input("enter the string\n")
vowels=0
consonants=0
for i in a:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
    else:
        consonants=consonants+1
        
print("total  number of vowels in the string is:",vowels)
print("total number of consonants in the string is:",consonants)
