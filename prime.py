num = int(input("enter the nunber: "))

if num <= 1:
    print(("it is not a prime number "))
else:
    for i in range(2,num):
        if num % i == 0:
            print("the number is not a prime number ")
            break
    else:
        print("the number is a prime")