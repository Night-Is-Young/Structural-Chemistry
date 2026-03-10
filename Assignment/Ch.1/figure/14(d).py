import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

l = 1001
lst = [0 for i in range (l)]
for nx in range(1,33):
    for ny in range(1,33):
        for nz in range(1,33):
            n = nx * nx + ny * ny + nz * nz
            if n < l:
                lst[n] += 1
for i in range(1,l):
    lst[i] += lst[i-1]


fig, ax = plt.subplots()
plt.step(range(l), lst, where='post', label=r"$\Phi(\epsilon)$")
x = np.linspace(0, 1000, 1000)
ax.plot(x, np.pi/6 * x**(3/2), label=r"$\Phi^{TF}(\epsilon)$")
plt.xlabel(r"$\epsilon/E_1$")
plt.ylabel(r"$\Phi(\epsilon)$")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.legend()
plt.show()