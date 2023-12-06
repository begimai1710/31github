#basic lambda
square = lambda x: x ** 2
print("Square:", square(4))


#with multiple characters
add = lambda x, y: x + y
print(add(3, 4))  # Output 7

#as an Argument to a Higher-Order Function:
# Sorting a list of tuples based on the second element
pairs = [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

#with map
numbers = [1, 2, 3]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
