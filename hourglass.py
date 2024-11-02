def hourglass_sum(arr):
    max_sum = float('-inf')  # Initialize max_sum to the smallest possible value
    for i in range(4):  # Loop through rows (0 to 3)
        for j in range(4):  # Loop through columns (0 to 3)
            # Calculate the hourglass sum
            current_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                arr[i + 1][j + 1] +
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )
            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

if __name__ == "__main__":
    arr = []

    # Read input
    for _ in range(6):
        row = list(map(int, input().strip().split()))
        arr.append(row)

    result = hourglass_sum(arr)

    # Print the result
    print(result)