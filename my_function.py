def swapUsingLenFunction(arr):
    lelement= len(arr)-1
    arr[0],arr[lelement] = arr[lelement],arr[0]
    return arr

def swapUsingNegativeIndex(arr):
    arr[0],arr[-1] = arr[-1],arr[0]
    return arr

def swapUsingStarOperand(arr):
    a,*b,c = arr
    return [c,*b,a]



print(swapUsingLenFunction([1,2,3,4,5,6]))
print(swapUsingNegativeIndex([1,2,3,4,5,6]))
print(swapUsingStarOperand([1,2,3,4,5,6]))
"""
x = x+ y
y = x - y
"""