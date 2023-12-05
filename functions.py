def greet(name):
  """This function greets the person passed in as a parameter."""
  print("Hello, " + name + "!")

# Call the function
greet("Bob")

#function with return value
def add_numbers(a, b):
  """This function returns the sum of two numbers."""
  return a + b

# Call the function and store the result
result = add_numbers(5, 3)
print("Sum:", result)

def power(base, exponent=2):
  """This function raises the base to the given exponent."""
  return base ** exponent

# Call the function with default exponent
result_default = power(2)
print("Default Exponent:", result_default)

# Call the function with a custom exponent
result_custom = power(2, 4)
print("Custom Exponent:", result_custom)

def calculate_sum(*args):
  """This function calculates the sum of a variable number of arguments."""
  total = 0
  for num in args:
      total += num
  return total

# Call the function with different numbers of arguments
result1 = calculate_sum(1, 2, 3)
result2 = calculate_sum(4, 5, 6, 7)
print("Result 1:", result1)
print("Result 2:", result2)

def factorial(n):
    """This function calculates the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
