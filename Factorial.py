def factorial(value):
    if abs(value) != 0:
        count = 1
        for i in range(1, value+1):
            count *= i
        return count
    else:
        return 1

print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
