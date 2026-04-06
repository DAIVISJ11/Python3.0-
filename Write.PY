try:
    with open('Codingal (1).txt', 'r') as file_read:
        print("FILE IN READ MODE- ")
        print(file_read.read)

except FileNotFoundError:
    print("Error: File not found!")

    #Write Mode 
with open('Codingal (1).txt', 'w') as file_write:
    file_write.write("\nFile in write mode .....\n")
    file_write.write("\nHello! We are learning about File Handling and have Davis i calss as the Student, and Dominic as the Teacher \n")

    #Append Mode
with open('Codingal (1).txt', 'a') as file_append:
    file_append.write("\nFile in write mode .....\n")
    file_append.write("\nHello! We are learning about File Handling  \n")
   





