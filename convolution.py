import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.integrate import quad
#defining unit step function
def u(t):
    return 1 if t>=0 else 0 

#defining continuous signal 
def x(t):
    return np.exp(t) if t<0 else 0

#defining impulse response
def h(t):
    return u(t-1)

#convolution 
def convolution_continuous(t):
    integrand = lambda tau: x(tau)*h(t-tau)
    result, _ = quad(integrand,-np.inf,np.inf)
    return result

# now we'll take sample values of t
t_values = np.linspace(-6,6,50)
convolu_values = [convolution_continuous(t) for t in t_values]

#plotting time hehe 
plt.figure(figsize=(9,9))
plt.plot(t_values,
convolu_values, label='x(t)*h(t)',color='blue')
plt.title('Convolution of Continuous Approximation')
plt.xlabel('t')
plt.ylabel('x(t)*h(t)')
plt.legend()
plt.savefig('plot.jpeg')
plt.show()


