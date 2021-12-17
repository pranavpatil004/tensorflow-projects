import matplotlib.pyplot as plt
import numpy as np
from time import sleep

fig = plt.figure()
ax = fig.add_subplot(111)

i = 0
x, y = [10], [11]
while True:
    x.append(i)
    y.append(i+10)
    
    if i > 100:
        break
    sleep(0.1)
    i += 1
ax.plot(x, y, color='b')
    
fig.canvas.draw()

ax.set_xlim(left=max(0, i-50), right=i+50)
plt.ion()
fig.show()

input('test')