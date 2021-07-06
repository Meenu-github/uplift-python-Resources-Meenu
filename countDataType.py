test_list = [3,1,0,'computer',True, False, 5, 'geeks', 6, 7, 2.3, 6.5]

print("The original list is : " + str(test_list))

intCount = len(list(i  for i in test_list if isinstance(i, int) and not isinstance(i, bool)   ))
strCount = len(list(i for i in test_list if isinstance(i, str)))
boolCount = len(list(i for i in test_list if isinstance(i, bool)))
floatCount = len(list(i for i in test_list if isinstance(i, float)))
print("The length of integers in list is : " + str(intCount))
print("The length of floats in list is : " + str(floatCount))
print("The length of strings in list is : " + str(strCount))
print("The length of boolean in list is : " + str(boolCount))

