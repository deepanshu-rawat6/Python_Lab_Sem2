dict = {}
list = []
list1 = []
for i in range(1, 3):
    states = input("Enter the state name: ")
    capital = input("Enter the state capital: ")
    population = int(input("Enter the population no: "))
    area = int(input("Enter the area of the state: "))
    dict[states] = [capital, population, area]
    list.append(population)
    list1.append(states)
print(list1)
c = 0
maximum = list[0]
for j in list:
    if maximum < j:
        maximum = j
p = list1.index(maximum)
sum = 0
print("The state with highest population is", p)
for k in list:
    sum = sum + k
print("The combined population of all states is", sum)
