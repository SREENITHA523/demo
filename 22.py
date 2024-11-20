
list= [2,3,4,5,6,7]
n=int(input("enter the value to search"))
for i in range(len(list)):
    if list[i]==n:
        print("found at index",i+1)
        break
else:
    print("not found")