import clr # the pythonnet module.
clr.AddReference(r'OpenHardwareMonitor\OpenHardwareMonitorLib') 
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0
x, y = [], []
'''c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()'''

    
'''while True:
    for a in range(0, len(c.Hardware[0].Sensors)):
        # print(c.Hardware[0].Sensors[a].Identifier)
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            x.append(i)
            #print(c.Hardware[0].Sensors[a].get_Value())
            new_y = c.Hardware[0].Sensors[a].get_Value()
            y.append(new_y)
            ax.plot(x, y, color='b')
    
            fig.canvas.draw()
    
            ax.set_xlim(left=max(0, i-50), right=i+50)
            c.Hardware[0].Update()
            i += 1
    sleep(0.1)'''