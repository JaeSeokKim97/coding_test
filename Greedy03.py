data = list(map(int, input()))
result = data[0]

for num in data[1:]:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)