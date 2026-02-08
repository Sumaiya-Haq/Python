n = int(input('Enter the number of process: '))
p, at, bt = [], [], []
nbt = []
tq = []
avtat, avwt, avc = [], [], []
print('Enter process:')
for i in range(n):
    p.append(input())
print('Enter Arrival time:')
for i in range(n):
    at.append(int(input()))
print('Enter Burst time:')
for i in range(n):
    a = int(input())
    bt.append(a)
    if a != 0:
        nbt.append(a)
minbt = min(nbt)
maxbt = max(nbt)
sortedp = sorted(range(n), key=lambda i: at[i])
for TQ in range(minbt, maxbt + 1):
    ct = [0] * n
    tat = [0] * n
    wt = [0] * n
    rt = bt.copy()
    gc = []
    gct = []
    que = []

    time = at[sortedp[0]]
    gct.append(time)
    first = sortedp[0]
    que.append(first)
    visited = [False] * n
    visited[first] = True

    while que:
        i = que.pop(0)
        gc.append(p[i])
        if rt[i] >= TQ:
            time += TQ
            rt[i] -= TQ
        else:
            time += rt[i]
            rt[i] = 0
        gct.append(time)
        for k in range(n):
            if at[k] <= time and not visited[k]:
                que.append(k)
                visited[k] = True
        if rt[i] == 0 and ct[i] == 0:
            ct[i] = time
        else:
            que.append(i)

    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
    avtat.append(sum(tat) / n)
    avwt.append(sum(wt) / n)
    tq.append(TQ)
    print(f'\nThis is for Time Quantum -- {TQ} ---')
    print("Process AT BT CT TAT WT")
    for i in range(n):
        print(p[i], at[i], bt[i], ct[i], tat[i], wt[i])
    print("\nGantt Chart:")
    for x in gc:
        print(f"| {x} ", end="")
    print("|")
    for t in gct:
        print(t, end="   ")
    print()

print("\nTime Quantum | Average WT | Average TAT")
for i in range(len(tq)):
    print(f"    {tq[i]}       |   {avwt[i]:.2f}    |   {avtat[i]:.2f}")
for i in range(len(avwt)):
    avc.append((avtat[i] + avwt[i]) / 2)
best = sorted(range(len(tq)), key=lambda i: avc[i])
print(f'\nBest time quantum is = {tq[best[0]]}')