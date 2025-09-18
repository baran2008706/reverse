str_1 = input("enter a string to get it's reversed: ")
result = ""

for index in range(len(str_1)-1, -1, -1):
    result += str_1[index]

print(result)