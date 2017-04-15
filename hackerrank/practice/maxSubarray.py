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

    """
    def MaxSub(A,N):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    if ( max_so_far == 0 ):
        max_so_far = max(A)
    return str( max_so_far )
    
def MaxSubNonCont(A,N):
    tot = 0
    for x in A:
        if (x > 0):
            tot += x
    if (tot == 0):
        tot = max(A)
    return str( tot )
    
T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    print( MaxSub(A,N) + " " + MaxSubNonCont(A,N) )
    

      """
      
