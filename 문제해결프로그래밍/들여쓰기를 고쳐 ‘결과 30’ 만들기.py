def sum_even(n):
    total= 0
    for value in range(1, n + 1):
        if value% 2== 0:
            total+= value
        if value == n:
            return total

print(sum_even(10))
