t=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter number to search:"))
i=0
found=False
while i<len(t):
    if t[i]==x:
        print("Number found at index",i)
        found=True
        break
    i=i+1
if found==False:
    print("Number not found")