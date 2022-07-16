import os

path = "path to folder"

files = os.listdir(path)

for i in range(len(files)):
	source = path + files[i]
	desti = path + str(i+1)
	os.rename(source,desti)