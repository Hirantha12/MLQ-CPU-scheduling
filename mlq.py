n = int(input("Enter the number of processes: "))

p = [0] * 30
bt = [0] * 30
su = [0] * 30
wt = [0] * 30
tat = [0] * 30
waiting_avg = 0.0
turnaround_avg = 0.0
tr = 0
csource = 0
cuser = 0
btsource = [0] * 30
btuser = [0] * 30
puser = [0] * 30
psource = [0] * 30

for i in range(n):
    tr = int(input("System process/User Process (0/1): "))
    bt_val = int(input(f"Enter the Burst Time of Process {i}: "))
    
    if tr == 1:
        btuser[cuser] = bt_val
        puser[cuser] = i
        cuser += 1
    elif tr == 0:
        btsource[csource] = bt_val
        psource[csource] = i
        csource += 1

for i in range(csource):
    p[i] = psource[i]
    bt[i] = btsource[i]
    su[i] = 0

for i in range(cuser):
    p[i + csource] = puser[i]
    bt[i + csource] = btuser[i]
    su[i + csource] = 1

print("PROCESS\tSYSTEM/USER PROCESS\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")

for i in range(n):
    print(f"{p[i]}\t\t{su[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

waiting_avg = wt[0] = 0
turnaround_avg = tat[0] = bt[0]

for i in range(1, n):
    wt[i] = wt[i - 1] + bt[i - 1]
    tat[i] = tat[i - 1] + bt[i]
    waiting_avg += wt[i]
    turnaround_avg += tat[i]

print(f"\nAverage Waiting Time is: {waiting_avg / n}")
print(f"Average Turnaround Time is: {turnaround_avg / n}")
