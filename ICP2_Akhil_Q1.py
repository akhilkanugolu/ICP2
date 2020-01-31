no_of_students=int(input("Enter Number of Students:"))
list_lb=[]
list_kg=[]
for i in range(no_of_students):
        print("Enter Lb Weight of", i+1 ,"Student:")
        lb_weight=int(input())
        list_lb.append(lb_weight)
        list_kg.append(lb_weight*(0.453514))

print("Weight of Students in lb",list_lb)
print("Weight of Students in kg",list_kg)
