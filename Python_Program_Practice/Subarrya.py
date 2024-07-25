A = [1, 2, 3, 7, 5]
n = 12
current_sum = 0
start = 0

for i, num in enumerate(A):
    current_sum += num

    # Adjust the start position if current_sum exceeds n
    while current_sum > n and start <= i:
        current_sum -= A[start]
        start += 1

    # Check if the current_sum equals n
    if current_sum == n:
        print([start, i])
        break
else:
    print("No subarray found")
