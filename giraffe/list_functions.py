

lucky_numbers = [2, 5, 1, 3, 6, 0]

friends = ["Marco0", "Polo1", "Ivan2", "John3", "Doe4", "Lovro5", "Mile6", "John3"]

print(friends)

for i in lucky_numbers:
    print(friends[i])

friends.append("Johnny")
friends.insert(1, "Inserted John")
friends.remove("Inserted John")

friends.extend(lucky_numbers)

print(friends)

friends.pop()
print(friends.index("Marco0"))
print(friends.index("Ivan2"))
print(friends.count("John3"))

print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends.clear()
print(friends)

lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)
