import os

# specify the directory ('.' means current directory)
directory = '/'

# list all files and directories
contents = os.listdir(directory)

print("Contents of directory:", directory)
for item in contents:
    print(item)
 