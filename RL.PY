with open ('Codingal (1).txt', 'r') as file1, open('CodingalUpdated.txt', 'w') as file2:
    for line in file1:
        if not line.startswith("The"):
            print(line.strip())
            file2.write(line)