n = int(input())
for i in range(n):
    num = int(input())
    string = str(num)
    length = len(string)
    sum = 0
    for i in range(length):
        number = string[i]
        sum += int(number) ** length
    if sum == num:
        print(num)
