def d(n):
    sum_of_digits= 0
    for digit in str(n):
        sum_of_digits += int(digit)
        return n + sum_of_digits

def f(n):
    return n+ sum(int(digit) for digit in str(n))

print(d(123),"\n",f(123))
