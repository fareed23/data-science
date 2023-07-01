# // How to make a line plot in Python?
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

ax.plot(x, y)

ax.set_title("Line Plot")
ax.set_xlabel("X-values")
ax.set_ylabel("Y-values")

plt.show()