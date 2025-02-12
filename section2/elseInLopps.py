my_list = []

x = int(input("Enter no. of elements: "))
print("\n")


for i in range(x):
    j = int(input("Enter element : "))
    print("\n")
    my_list.append(j)


for i in my_list:
    if i == 0:
        break
    print(i)


else:
    print("all elements printed success4fully")
