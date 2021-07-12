car_list = input("Enter the list : ")
car_list =  car_list.split()
def overtake():
    overtaken = 0
    overtaken = sum([(overtaken+1) for i in range(len(car_list)) for j in range(i+1,len(car_list)) if (car_list[i]>car_list[j])])
    return overtaken

print(overtake())
