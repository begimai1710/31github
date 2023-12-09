try:
  import POOP
except ImportError:
  print ("Oops! Poops")

try:
  import BOB
except Exception:
  print ("Not Bob")

try:
  import BOB
except ValueError:
  print ("Not Bob")

try:
  import BadPasta 
except SyntaxError:
  print ("I love you anyways")

russianDict = {'shishka': 'pinecone'}
englishDict = {'pinecone': 'shishka'}
try:
  russianDict["MY KING"]
except KeyError:
  print ("no queen, not here")

  while True:
  try:
      x = int(input("Please enter a number: "))
      break
  except ValueError:
      print("Oops!  That was no valid number.")