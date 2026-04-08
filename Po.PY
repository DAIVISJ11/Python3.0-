with open('Codingal (1).txt', 'r') as file:
    print("File in read mode: -")
    print(file.read())

with open ('Codingal (1).txt', 'w') as file:
    file.write("File in write mode:")
    file.write(" The content is amazing")


with open ('Codingal (1).txt', 'a') as file:
    file.write(" \nFile in append mode...:\n")
    file.write(" \nWelcome to codingal \n")
