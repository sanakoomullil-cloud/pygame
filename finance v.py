import matplotlib.pyplot as plt
import numpy as np

m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
inc = [4500, 4800, 5100, 5000, 5300, 5500]
exp = [4000, 4100, 4300, 3900, 4200, 4400]
cats = ['Rent', 'Food', 'Util', 'Fun']
x = np.arange(len(cats))

plt.style.use('default') 
fig, axs = plt.subplots(2, 2, figsize=(10, 7), facecolor='white')

axs[0, 0].plot(m, inc, 'g-o', label='Inc')
axs[0, 0].plot(m, exp, 'r-s', label='Exp')
axs[0, 0].set_title('Income vs Expenses')
axs[0, 0].legend()
axs[0, 0].set_facecolor('white')

axs[0, 1].bar(m, [i - e for i, e in zip(inc, exp)], color='blue')
axs[0, 1].set_title('Savings')
axs[0, 1].set_facecolor('white')

axs[1, 0].bar(x - 0.2, [1500, 600, 300, 400], 0.4, label='Bud', color='orange')
axs[1, 0].bar(x + 0.2, [1500, 650, 280, 450], 0.4, label='Act', color='cyan')
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(cats)
axs[1, 0].legend()
axs[1, 0].set_facecolor('white')

axs[1, 1].stackplot(m, [1500]*6, [600, 610, 620, 600, 630, 640], labels=['Rent', 'Food'], colors=['pink', 'purple'])
axs[1, 1].set_title('Spending Split')
axs[1, 1].legend(loc='upper left')
axs[1, 1].set_facecolor('white')

plt.tight_layout()
plt.savefig('personal_finance_visualiser.png')
plt.show()




