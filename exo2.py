num = input("please enter a number ")
print(num)
check = input("/ ")


if int(num)%int(check) == 0:
    print("The second number divide the first evenly ")
elif int(num)%4 == 0:
    print("the first number is a multiple of 4")

else: 
    print("the second number doesn/'t divide the first evenly ")
