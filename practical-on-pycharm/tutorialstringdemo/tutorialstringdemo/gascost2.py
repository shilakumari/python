n=5
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
tank=0
station=-1
for i in range(n):
    tank = gas[i]
    print("tank",tank)
    c = 0
    g = 0
    n1=0
    j1=-1
    for j in range(i+1, n):
        n1+=1
        tank = tank - cost[j-1] + gas[j]
        #print("j",j, "tank", tank, " cost", c, " gas", g, end=' ')
        #tank = tank - c + g
        print("j",j,"tank - c + g ",tank)
        j1=j
    if i !=0 or n1 < n:
        for k in range((n-n1)):
            if k==0:
                tank = tank - cost[j1] + gas[k]
            else:
                tank = tank - cost[k-1] + gas[k]

            print("k", k, "tank - c + g ", tank)
            #print("k",k, "tank", tank, " cost", c, " gas", g)
            if k==i and tank>gas[k]:
                station = k
                print("station",station)
                break

        print()

print(station)
