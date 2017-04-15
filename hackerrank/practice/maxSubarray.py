for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = a[0]
    cur = a[0]

    for i in range(1, n):
        cur = max(cur + a[i], a[i])
        ans = max(ans, cur)

    a = sorted(a, reverse=True)
    ans2 = a[0]
    for i in range(1, n):
        if a[i] > 0:
            ans2 += a[i]
    print(ans, ans2)
