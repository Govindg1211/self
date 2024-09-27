def generate_2d_array(X, Y):
    return [[i*j for j in range(1, Y+1)] for i in range(1, X+1)]

X = int(input("Enter X: "))
Y = int(input("Enter Y: "))

result = generate_2d_array(X, Y)

for row in result:
    print(row)
