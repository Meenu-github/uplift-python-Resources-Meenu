lis = [[1,2], [3,4] ,[5,6] ,[7, 8, 9]]
tup = [list((11,12)), list((13,14)), list((15,16)), list((17, 18, 19))]

opList = []


def opList1(lis,tup):
    for i in range(8):
        if (i%2==0):
            opList.append(tup[int(i / 2)])
            

        if (i%2!=0):


            opList.append(lis[int(i / 2)])
            

    return opList
def opList2(lis,tup):
    for i in range(8):
        if (i%2==0):

            opList.append(lis[int(i/2)])
        if (i%2!=0):

            opList.append(tup[int(i/2)])
    return opList
usIp = int(input("Enter 1 for tuple and 2 for list : "))
if usIp==1:
    print(opList1(lis,tup))
elif usIp==2:
    print(opList2(lis,tup))
else :
    print("WRONG INPUT SORRY !!!")
    exit()

for i in range(len(opList)):
    for j in range(len(opList[i])):
        print(opList[i][j], end="  ")
