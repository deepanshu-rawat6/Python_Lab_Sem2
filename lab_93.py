f = open("f1.txt", "r")
file = f.read()
s = ''
try:
    for i in file:
        if i == '"':
            s = s + "\\"
        s = s + 1
    print(s)
except Exception as x:
    print("An error has occurred of type", x.__class__)
