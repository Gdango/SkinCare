import get_info
import matplotlib.pyplot as plt
import numpy as np

info = get_info.get_info('SELECT brand, count(brand) As num_prod, AVG(rating) As avg_rating from combination where rating >= 4 group by brand order by num_prod desc;')

fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(np.arange(1, 11), info[0][0:10])  #get the top 10
#ax.set_xticks(range(1, 11),1)
plt.xticks(np.arange(1, 11, 1))
ax.set_xticklabels(info[1][0:10])
plt.xlabel('Brand Name')
plt.ylabel('Number of Product')
plt.title('Top 10 Brand with Product the Most Product Greater Than 4 Stars')

plt.show()