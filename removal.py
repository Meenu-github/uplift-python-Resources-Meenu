lis = input("Enter the list : ")
lis = lis.split(" ")
newlis = []
k = int(input("Enter the number for removal : "))

for i in range(len(lis)):
    if int(lis[i])!=k:
        newlis.append(int(lis[i]))
    

print(newlis)