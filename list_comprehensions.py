squares = [x**2 for x in range(10)]
print (squares)

evens = [x for x in range(10) if x % 2 == 0]
print (evens)

even_squares = [x**2 for x in range (10) if x % 2 == 0]
print (even_squares)

sentence = "This is the github challenge"
word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)

word = "This is Begimai"
uppercase_letters = [letter.upper() for letter in word]
print(uppercase_letters)
