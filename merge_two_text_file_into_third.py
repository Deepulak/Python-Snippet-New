# Program to merge two files into third

# open file1 in read mode

with open('file1.txt') as file1:
	text1 = file1.read()
	# and reads its content

# opne file2 in read mode

with open('file2.txt') as file2:
	text2 = file2.read()

# open file3 in write mode
with open('file3.txt', 'w') as file3:
	file3.write(text1+'\n'+text2)
	# and write all the content to it

# so for run this program we need total three file in
# our system

# or folder/ directory

