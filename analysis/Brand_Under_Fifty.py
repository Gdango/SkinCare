import get_info
import matplotlib.pyplot as plt
import numpy as np

query = 'select brand, avg(max_amount) from combination where rating >= 4 group by brand order by avg(max_amount) desc;'

info = get_info.get_info(query)

cost = info[0]
brand = info[1]

def graph_info(cost, brand, ind, i):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(np.arange(ind+1, i+1), cost[ind:i])
    plt.xticks(np.arange(ind+1, i+1, 1), rotation = 'vertical')
    ax.set_xticklabels(brand[ind:i])
    ax.set_xlabel('Brand Name')
    ax.set_ylabel('Average Cost')
    ax.set_title('Average Cost for Brand Greater Than 4 Stars')
    plt.show()

cost60 = 0
cost50 = 0
cost0 = 0

for i in range(0,len(cost)):
    if cost[i] >= 60:  # if cost is greater than 100 dollars
        cost60 = i
    elif cost[i] >= 30:
        cost50 = i
    elif cost[i] >= 0:
        cost0 = i
# 0 20 75

graph_info(cost, brand, 0, cost60)
graph_info(cost, brand, cost60, cost50)
graph_info(cost, brand, cost50, cost0)

