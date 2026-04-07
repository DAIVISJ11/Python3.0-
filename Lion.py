print("Today we will be talking about Lions")
try:
    with open('lion__8_mammals___discovering_wildlife_fact_file_by_ajolley785727_dg62vgy-fullview.jpg', 'r') as file:
        content = file.read()
        print("File Content: \n")
        print(content)

except FileNotFoundError:

    print("Error: The File 'Codingal (1).txt' was not found")