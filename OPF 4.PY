with open("Codingal (1).txt", "w") as file:
    file.write("Did you know that chicken strips are generally better than chicken nuggets") 


with open ("Codingal (1).txt", "r") as file:
    print("words in this file are ...")

    for line in file:
        words =line.split()
        print(words)


import os
#creating a new file

try:
    with open(" New_file.txt", "x") as new_file:
        pass
    print("New_file.txt creating successfully")

except FileExistsError:
    print("New_file.txt already exists")

with open ('Codingasl (1).txt', 'r') as file:
    print("\n Full content: \n")
    print(file.read())


with open('Codingasl (1).txt', 'r') as file:
    print("\n Reading the first 13 characters \n")
    print(file.read(13))

    with open('Codingasl (1).text', 'a') as file:
        file.write('\n oday we will be taling about football and other sports \n')



#checking if a file exists
print("Checking if my_file,txt exists or not...")
if os.path.exists("my_file.txt"):
    os.path.remove("my_file.txt")
    print("my_file.text deleted")

else:
    print("The file does not exists")
  

#deleting a file
if os.path.exists("Codingal (1).txt"):
    os.remove("Codingasl (1).txt")
    print("Codingal (1).txt deleted")

else:
    print("Codingal (1).txt does not exists")