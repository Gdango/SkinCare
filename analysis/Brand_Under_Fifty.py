import get_info
import matplotlib.pyplot as plt
import numpy as np

query = 'select brand, round(max(max_amount)) from combination group by brand order by avg(max_amount) desc;'

info = get_info.get_info(query)

fig = plt.figure()
ax = fig.add_subplot(111)
x = info[0]
plt.bar(np.arange(1, len(x) + 1), info[0])  #get the top 10
#ax.set_xticks(range(1, 11),1)
plt.xticks(np.arange(1, len(x)+1, 1))
ax.set_xticklabels(info[1])
plt.xlabel('Brand Name')
plt.ylabel('Average Cost')
plt.title('Average Price of Each Brand with Product Greater Than 4 Stars')

plt.show()