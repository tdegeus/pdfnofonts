import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([0, 2], [0, 2])
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.savefig('fig1.pdf')
plt.close()
