test_list = [2, 1.2, 1.4,'hello', 'nice', True, False]
print("The original list is : " + str(test_list))

intCount = len(list(i  for i in test_list if isinstance(i, int) and ((i!=True) and (i!=False))))
strCount = len(list(i for i in test_list if isinstance(i, str)))
boolCount = len(list(i for i in test_list if isinstance(i, bool)))
floatCount = len(list(i for i in test_list if isinstance(i, float)))
print("The length of integers in list is : " + str(intCount))
print("The length of floats in list is : " + str(floatCount))
print("The length of strings in list is : " + str(strCount))
print("The length of boolean in list is : " + str(boolCount))
