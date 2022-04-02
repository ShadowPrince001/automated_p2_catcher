from pokemon_list import pokemon_list

name = "M__"
length = len(name)
count = 0
for a in name:
    if (a.isalpha()) == True:
        count += 1
counter = 0
for a in pokemon_list:
    if length == len(a):
        for r in range(length):
            if name[r] is a[r]:
                counter += 1
        if counter == count:
            print(name, "is", a)
            counter = 0
        else:
            counter = 0
