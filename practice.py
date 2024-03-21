import os 

file_path = os.path.join("data", os.listdir("data")[0])


file_extension = os.path.splitext(file_path)[1].lower()

print(file_extension)

