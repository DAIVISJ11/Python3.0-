with open("Codingal (1).txt", "w") as file:
    file.write("file operations are essential actions for managing data, including creating, opening, reading, writing, updating and deleting files to store information pamanently")


with open ("Codingal (1).txt", "r") as file:
    print("words in this file are ...")

    for line in file:
        words =line.split()
        print(words)