f = open("abc.txt", "r")
print(f.read(10))
print(f.tell())
f.seek(12)
print(f.read())
f.seek(0)
print(f.readline())
f.seek(0)
for line in f:
    print(line, end='')
print(list(f))
f.close()
# f.read() gives an error because f.close() stops any more operations to be executed on a file
