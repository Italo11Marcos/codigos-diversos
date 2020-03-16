def fat(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat

while True:
    n = input().strip()
    if n == '0':
        break
    N = len(n)
    resp = fat(N)
    print(resp)
