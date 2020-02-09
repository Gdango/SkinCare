import get_info
import matplotlib.pyplot as plt
import numpy as np

query = 'select brand, round(max(max_amount)) from combination group by brand order by avg(max_amount) desc;'

info = get_info.get_info(query)

fig = plt.figure()
ax = fig.add_subplot(211)
x = info[0]
plt.bar(np.arange(1, 11), info[0][0:10])#get the top 10
#ax.set_xticks(range(1, 11),1)
plt.xticks(np.arange(1, 11, 1))
ax.set_xticklabels(info[1][0:10])

ax2 = fig.add_subplot(212)
plt.bar(np.arange(1,11), info[0][10:20])
plt.xticks(np.arange(1, 11, 1))
ax2.set_xticklabels(info[1][10:20])

plt.xlabel('Brand Name')
plt.ylabel('Average Cost')
plt.title('Average Price of Each Brand with Product Greater Than 4 Stars')

plt.show()