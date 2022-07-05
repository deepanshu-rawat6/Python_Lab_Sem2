f = open('jingle.txt', 'r+')
l = f.read().lower()
l = l.split()
cont = {}
for i in l:
    if i not in cont:
        cont[i] = 1
    else:
        cont[i] += 1


f2 = open('words.txt', 'w+')
for key, value in cont.items():
    f2.write('%s:%s\n' % (key, value))
