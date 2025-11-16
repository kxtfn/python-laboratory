import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 100)
y = x ** np.sin(10 * x)

plt.plot(x, y, label='y = x^sin(10x)', color='green', linewidth=3, linestyle='-')  # суцільна лінія зеленого кольору товщиною 3
plt.title('Графік функції y(x) = x^sin(10x)', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()
