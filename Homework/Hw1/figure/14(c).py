import matplotlib.pyplot as plt

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

l = 31
lst = [0 for i in range (l)]
for nx in range(1,15):
    for ny in range(1,15):
        for nz in range(1,15):
            n = nx * nx + ny * ny + nz * nz
            if n < l:
                lst[n] += 1
for i in range(1,l):
    lst[i] += lst[i-1]
x = range(len(lst))

fig, ax = plt.subplots()
plt.step(x, lst, where='post')  # 阶梯图
plt.xlabel(r"$\epsilon/E_1$")
plt.ylabel(r"$\Phi(\epsilon)$")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
plt.show()