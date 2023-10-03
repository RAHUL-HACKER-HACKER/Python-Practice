def sqrt_without_builtin(x):
    guess = x
    while abs(x-guess*guess) > 3:
        guess = (guess + x / guess) / 2
    return guess

# Example usage
number = float(input("Enter a number: "))
result = sqrt_without_builtin(number)
print(result)
