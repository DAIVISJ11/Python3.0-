try:
    with open('Codingal (1).txt', 'r') as file:
        content = file.read()
        print("File Content: \n")
        print(content)

except FileNotFoundError:

    print("Error: The File 'Codingal (1).txt' was not found")