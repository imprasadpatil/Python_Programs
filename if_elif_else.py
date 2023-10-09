//Unit 2 Assignment 
//Q.2 - B

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("multiple of both ")
    elif num % 3 == 0:
        print("multiple of 3")
    elif num % 5 == 0:
        print("multiple of 5")
    else:
        print(num)
