sum = 0

for i in range(1,51):
    if i%2==0:
        sum += i
    else:
        continue
print("the sum of all the numbers is: ", sum)