isRainy = True
isCloudy = True
isSunday = True
isWorkDay = False

if isWorkDay:
  print("it is a workday!")
elif isRainy:
  print("it is rainy!")
  if isSunday:
    print("it is sunday!")
  else:
    print("it is not sunday :(")
  print('abracadabra')
elif isSunday:
  print("it is sunday!")
else: 
  print("i don't know!")

isCute = True
isPretty = True

if isCute:
  print("the puppy is cute!")

if isPretty:
  print("the puppy is pretty!")

  dictionary = {"shishka": "pinecone", "mishka": "bear"}

print("Translate correctly!")

print("What is mishka?")

userAnswer = input("Mishka is... ")
if userAnswer == dictionary["mishka"]:
  print("Correct! Mishka is ", dictionary["mishka"])
else:
  print("Incorrect! Mishka is ", dictionary["mishka"])

  #Write a Python program that takes a student's score as input and prints their grade according to the following criteria:

#Score 90 or above: A
#Score 80 to 89: B
#Score 70 to 79: C
# Score 60 to 69: D
# Score below 60: F

score= 88
if score >= 90:
  print("A")

elif score >= 80 and score <= 89:
  print("B")

elif score >=70:
  print("C")

elif score >=60:
  print ("D")
else:
  print("F")