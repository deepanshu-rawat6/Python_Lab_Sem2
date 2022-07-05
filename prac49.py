f = open("apple1.txt", "r")
ptr = f.read().split()
maximum = 0
word = ""
for i in ptr:
    if maximum < len(i):
        maximum = len(i)
print("The longest word/words:")
for j in ptr:
    if len(j) == maximum:
        print(j)
print("Length of the largest word/words:", maximum)
f.close()
