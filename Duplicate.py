ourList = [10,20,30,40,50,60,10,60,40]

def repeatElement(x):
    size = len(x)
    repeatedElementsInLIst = []
    for i in range(size):
        k = i+1
        for j in range(k,size):
            if(x[i]==x[j] and x[i] not in repeatedElementsInLIst):
                repeatedElementsInLIst.append(x[i])
    return repeatedElementsInLIst
print(repeatElement(ourList))