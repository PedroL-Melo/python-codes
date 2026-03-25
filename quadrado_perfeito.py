list = []
for values in range(1, 11):
    list.append(values ** 2)
print(list)

#ou pode usar as "list comprehension"

list2 = [values**2 for values in range(1, 11)]
print(list2)