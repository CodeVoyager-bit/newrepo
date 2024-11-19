t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    l=[]
    sumi=0
    dis = []
    for i in arr:
        sumi+=i
        l.append(sumi)
    for i in range(n):
        minus = 0
        sum=l[i]
        if i >= k:
            minus = arr[i-k] + dis[i-(k+1)]
            dis.append(minus)
        else:
            dis.append(0)
        print(sum - minus, end = " ")
    print()
