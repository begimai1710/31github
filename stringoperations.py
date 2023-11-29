# Concatenation
str1 = "Hi"
str2 = "Queen"
result = str1 + ", " + str2
print(result)
# Output: Hi, Queen

# String Repetition
str_repeat = "Run, Begi, Run! " * 2
print(str_repeat)


# String Length
text = "Kyrgyzstan"
length = len(text)
print(length)

# Accessing Characters by Index
message = "BEGIMAI"
first_char = message[0]
print(first_char)

# Slicing
phrase = "Salam, Bishkek!"
sliced_text = phrase[7:15]
print(sliced_text)

#String Methods
text = "i am a teacher"
print(text.upper())      
print(text.lower())      
print(text.capitalize())  

# String formatting
name = "Begimai"
age = 23
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print(formatted_text)

# Checking substrings
sentence = "Bishkek is the capital of Kyrgyzstan"
is_capital_in_sentence = "capital" in sentence
print(is_capital_in_sentence)

# Replacing substrings
original_text = "I like Turkey"
modified_text = original_text.replace("Turkey", "Sweden")
print(modified_text)