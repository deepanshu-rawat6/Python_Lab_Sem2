with open('D:\VS CODE\PYTHONLAB/abc.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end='')
        line = reader.readline()
