from os import walk
filenames = next(walk("templates"))[2]
print(filenames)