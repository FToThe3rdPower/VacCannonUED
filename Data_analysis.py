import numpy as np
import matplotlib.pyplot as plt
#import os

txt = 'L_t4.txt'

nl = sum(1 for _ in open(txt))
#print(nl)

D = np.loadtxt(fname = txt ,skiprows = 3, max_rows = nl-4 ,  delimiter = ',')
t, v, f = D.T

plt.figure()
plt.plot(t, v, '.')
plt.xlabel('Time, s')
plt.ylabel('Velocity, m/s')
plt.title('Time vs Velocity')
plt.grid()
plt.savefig('Time.png')
plt.show()


plt.figure()
plt.plot(f, v , '.')
plt.xlabel('Frames')
plt.ylabel('Velocity, m/s')
plt.title('Frames vs Velocity')
plt.grid()
plt.savefig('Frames.png')
plt.show()