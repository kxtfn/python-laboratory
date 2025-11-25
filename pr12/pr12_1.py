import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 13*np.pi, 300)

line1, = ax.plot(x, np.sin(x), label='Синусоїда')
line2, = ax.plot(x, np.cos(x), label='Косинусоїда')

ax.set_ylim(-2, 2)
ax.legend()

def update(frame):
    # Амплітуда коливається між 0.5 і 1.5
    amp1 = 1 + 0.5 * np.sin(0.1 * frame)
    amp2 = 1 + 0.5 * np.cos(0.1 * frame)
    # Фаза змінюється лінійно з коливанням
    phase1 = 0.5 * np.sin(0.05 * frame)
    phase2 = 0.5 * np.cos(0.05 * frame)
    
    y1 = amp1 * np.sin(x + phase1)
    y2 = amp2 * np.cos(x + phase2)
    
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    return line1, line2

ani = FuncAnimation(fig, update, frames=np.arange(0, 400), interval=30, blit=True)
plt.show()
