apartmentapartment= {'alice' : 72, 'bob' : 69, 'charlie' : 80, 'david' : 75}
print(apartment)
print(apartment.keys())
print(apartment.values())

print(apartment['bob'])
apartment['chris'] = 90
print (apartment.values())
del apartment['bob']
print(apartment)
apartment['alice'] = 16
print(apartment.values())

print ('bob' in apartment)
print ('bob' not in apartment)= {'alice' : 72, 'bob' : 69, 'charlie' : 80, 'david' : 75}
print(apartment)
print(apartment.keys())
print(apartment.values())

print(apartment['bob'])
apartment['chris'] = 90
print (apartment.values())
del apartment['bob']
print(apartment)
apartment['alice'] = 16
print(apartment.values())

print ('bob' in apartment)
print ('bob' not in apartment)

russianDict = {'shishka': 'pinecone'}
englishDict = {'pinecone': 'shishka'}


bigDictionary = {}
bigDictionary['russian'] = russianDict
bigDictionary['english'] = englishDict


print(bigDictionary)
print(bigDictionary['russian']['shishka'])
# print(dictionary['shishka'])


aliceInfo = {'age': 19, 'height': 170, 'sex': 'f'}

apartment = {'alice': aliceInfo}
print(apartment['alice']['height'])
