
parrot = "Norwegian Blue"
print(parrot)

print(parrot[-4:-2])
print(parrot[-4:12])

#step
print(parrot[0:6:2])

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])