lis = []
tup = []
outputList = []
totalTupAndList = 0
def dynamicTupleAndListProblem():
    tupNo = int(input("Enter the number of tuples you want : "))
    for i in range(tupNo):
        subTup = []
        eleNo = int(input("Enter the number of element you want in the " + str(i + 1) + "th tuple : "))
        for j in range(eleNo):
            element = int(input("Enter the element for the tuple :  "))
            subTup.append(element)
        tup.append(tuple(subTup))
    listNo = int(input("Enter the number of list you want : "))
    for i in range(listNo):
        subLis = []
        eleNo = int(input("Enter the number of element you want  in the " + str(i + 1) + "th list : "))
        for j in range(eleNo):
            element = int(input("Enter the element for list : "))
            subLis.append(element)
        lis.append(subLis)
    totalTupAndList = tupNo + listNo
    userip = int(input("Enter 1 for having tuple first 2 for having list first : "))
    if userip == 1:
        if len(tup)<len(lis):
            for i in range(totalTupAndList):
                if i<len(tup):
                    outputList.append(tup[i])
                    outputList.append(lis[i])
                if i>= len(tup):
                    remLis = lis[i: ]
                    outputList.append(remLis)
                    break
        elif len(lis)<len(tup):
            for i in range(totalTupAndList):
                if i<len(lis):
                    outputList.append(tup[i])
                    outputList.append(lis[i])
                if i>=len(lis):
                    remLis = tup[i:] 
                    outputList.append(remLis)
                    break
        elif len(lis)==len(tup):
            for i in range(int(totalTupAndList/2)):
                outputList.append(tup[i])
                outputList.append(lis[i])
    elif userip == 2:
        if len(tup) < len(lis):
            for i in range(totalTupAndList):
                if i < len(tup):
                    outputList.append(lis[i])
                    outputList.append(tup[i])
                if i>=len(tup):
                    remLis = lis[i: ]
                    outputList.append(remLis)
                    break
        elif len(lis) < len(tup):
            for i in range(totalTupAndList):
                if i < len(lis):
                    outputList.append(lis[i])
                    outputList.append(tup[i])
                if i>= len(lis):
                    remLis = tup[i: ]
                    outputList.append(remLis)
                    break
        elif len(lis)==len(tup):
            for i in range(int(totalTupAndList/2)):
                outputList.append(lis[i])
                outputList.append(tup[i])
    else:
        print("SORRY! The value is not a valid option.")
    return outputList

print(dynamicTupleAndListProblem())

