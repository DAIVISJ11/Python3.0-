import os
#creating a new file

try:
    with open(" New_file.txt", "x") as new_file:
        pass
    print("New_file.txt creating successfully")

except FileExistsError:
    print("New_file.txt already exists")

#checking if a file exists
print("Checking if my_file,txt exists or not...")
if os.path.exists("my_file.txt"):
    os.path.remove("my_file.txt")
    print("my_file.text deleted")

else:
    print("The file does not exists")
  

#deleting a file
if os.path.exists("Codingasl (1).txt"):
    os.remove("Codingasl (1).txt")
    print("Codingasl (1).txt deleted")

else:
    print("Codingasl (1).txt does not exists")