a = int(input('물건가격 : '))
b = int(input('받은돈 : '))

n = b - a
count = 0
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)
