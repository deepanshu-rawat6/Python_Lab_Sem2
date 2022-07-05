a = [1, 2, 3, "4", 5]
s = 0
try:
    for i in a:
        s = s + i
    print('sum:', s)
    print(a[5])
except Exception as e:
    print("Error Code:", e)
