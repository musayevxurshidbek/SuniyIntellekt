a = int(input("A = "))
b = int(input("B = "))
toq = (a % 2 == 1) and (b % 2 == 1)
juft = (a % 2 == 0) and (b % 2 == 0)
print(toq or juft)