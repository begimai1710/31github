numbers = [5, 2, 1, 3, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  

numbers = [5, 2, 1, 3, 9]
sorted_numbers_desc = sorted(numbers, reverse= True)
print(sorted_numbers_desc)  

numbers = [5, 2, 1, 1, 9]
numbers.sort()
print(numbers)  

# Adding elements to the list
letters = ["a", "b", "c"]
letters.append("f")
print(letters)  

fruits = ["apple", "banana", "orange"]
fruits.insert(2, "cherry")  
print(fruits) 

colors = ["red", "green", "blue"]
print(colors[0])  

colors = ["red", "green", "blue"]
print(colors[-2])  

numbers = [0, 1, 2, 3, 4, 5]
subset = numbers[1:4]  
print(subset) 