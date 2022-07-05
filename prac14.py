num=[1,2,3,4,5,6,7,8,9,10]

def even(x):
    return x%2==0

ans=list(filter(even,num))

print(ans)