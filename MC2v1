import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def E(x):
    return x**6-9*x**4+20*x**2+0.25
def prob(E):
    return np.exp(-E/0.6)

x = np.linspace(-2.5,2.5,1500)
plt.plot(x,E(x))
plt.grid(True)
plt.show()

x1 = np.linspace(-2.5,-1.21,500)
x2 = np.linspace(-1.21,1.21,500)
x3 = np.linspace(1.21,2.5,500)

K1_ref = prob(min(E(x3))-min(E(x2)))
K2_ref = prob(min(E(x2))-min(E(x1)))

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

print(K1_ref,K2_ref)

dom1 = 0
dom2 = 0
dom3 = 0

for i in akcptd:
    if -2.5 < i < -1.21:
        dom1 += 1
    elif -1.21 < i < 1.21:
        dom2 += 1
    elif 1.21 < i < 2.5:
        dom3 += 1   
        
K1_exp = dom3/dom2
K2_exp = dom2/dom1

print(K1_exp,K2_exp)
