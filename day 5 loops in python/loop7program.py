t=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter number to search:"))
for i in range(len(t)):
    if t[i]==x:
        print("Number found at index",i)
        break
else:
    print("Number not found")
    