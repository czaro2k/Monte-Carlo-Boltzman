import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def E(x):
    return 0.04*(x**4-12*x**2+5*x+0.2)
def prob(E):
    return np.exp(-E/0.6)

x = np.linspace(-4,4,1000)
plt.plot(x,E(x))
plt.grid(True)
plt.show()

x1 = np.linspace(-4,0,500)
x2 = np.linspace(0,4,500)
K_ref = prob(min(E(x2))-min(E(x1)))

akcptd = []
not_akcptd = []

x_str = np.random.choice(x)
pot_str = E(x_str)
while len(akcptd) < 10000:
    x_new = x_str + st.norm.rvs(loc=0,scale=0.2)
    pot_new = E(x_new)
    d_pot = pot_new - pot_str
    if prob(d_pot) < st.uniform.rvs():
        not_akcptd.append(x_new)
        x_str = x_new
        if len(not_akcptd) > 40:
            x_str = np.random.choice(x)
    elif prob(d_pot) >= st.uniform.rvs():
        akcptd.append(x_new)
        x_str = x_new
        pot_str = pot_new

plt.hist(akcptd,bins=100,density=1)
plt.show()

pos = 0
neg = 0

for i in akcptd:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
K = pos/neg    

print('K_ref = ', K_ref)
print('K_sym = ', K)
        
