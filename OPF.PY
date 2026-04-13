with open ('Codingasl (1).txt', 'r') as file:
    print("\n Full content: \n")
    print(file.read())


with open('Codingasl (1).txt', 'r') as file:
    print("\n Reading the first 12 characters \n")
    print(file.read(12))

    with open('Codingasl (1).text', 'a') as file:
        file.write('\n oday we will be taling about football and other sports \n')
