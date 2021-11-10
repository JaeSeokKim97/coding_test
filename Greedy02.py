n, k = map(int, input().split())
count = 0

# while(n!=1):
#     if n % k == 0:
#         n //= k
#         count += 1
#     else:
#         n -= 1
#         count += 1

while True: # 시간복잡도를 줄일 수 있다
    # N이 K로 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    count += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 뺴기
count += (n-1)
print(count)
