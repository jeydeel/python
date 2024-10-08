import os
path=os.getcwd()+"/My_folder"
if not os.path.exists(path):
    os.makedirs(path)
else:
    print("File already exists")
filename = "/My_txt1.txt"
with open(path+filename,"a") as file:
    file.write("hello, world")
    
filename = "/my_poem.txt"
with open(path+filename, "r") as file:
    data = [lines.rstrip() for lines in file]
    print(data)
    
