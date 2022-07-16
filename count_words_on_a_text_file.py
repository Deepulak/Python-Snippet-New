file = open("address.txt", "rt")
data = file.read()
words = data.split()

print("Words in text file : ", len(words))
