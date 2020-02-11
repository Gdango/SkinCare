import get_info
import matplotlib.pyplot as plt
import numpy as np

query = 'select brand, avg(max_amount) from combination group by brand order by avg(max_amount) desc;'

info = get_info.get_info(query)

cost = info[0]
brand = info[1]

def graph_info(cost, brand, ind, i):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(np.arange(1, i+1), cost[ind:i])
    plt.xticks(np.arange(1, i+1, 1))
    ax.set_xticklabels(brand[ind:i])
    plt.show()

cost100 = 0
cost50 = 0
cost0 = 0

for i in range(0,len(cost)):
    print("YE")
    if cost[i] >= 100:
        
        if cost100 > cost[i]:
        cost100 = i
        graph_info(cost, brand, 0, cost100)
    elif cost[i] >= 50 and cost100 > i:
        cost50 = i
        graph_info(cost, brand, cost100, cost50)
    elif cost[i] >= 0 and cost0 > i:
        print("Yes")
        cost0 = i
        graph_info(cost, brand, cost50, cost0)




'''
#plt.subplot(212)
ax0.bar(np.arange(1,top+1), info[0][top:top*2])
plt.xticks(np.arange(1, top+1, 1))
ax0.set_xticklabels(info[1][top:top*2])

ax1.set_xlabel('Brand Name')
ax1.set_ylabel('Average Cost')'''
