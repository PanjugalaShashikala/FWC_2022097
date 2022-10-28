import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad
#defining function
def f(x):
	return (x*(np.exp(x)-1)*(x-1)*((x-2)**3)*((x-3)**5))
def f2(x):
        y,e = quad(f, -1, x)
        return y

def F(x):
	res = np.zeros_like(x)
	for i,val in enumerate(x):
		y,err = quad(f,-1,val)
		res[i]=y
	return res

#defining derivative of f(x)
df=lambda x: x*(np.exp(x)-1)*(x-1)*((x-2)**3)*((x-3)**5)    

#for minima using gradient descent
cur_x=0.5
precision=0.000000001
alpha=0.0001
max_iters=100000000
previous_step_size=1
iters=0

while (previous_step_size>precision)&(iters<max_iters):
	prev_x=cur_x
	cur_x-=alpha*df(prev_x)
	previous_step_size=abs(cur_x-prev_x)
	iters+=1
min_val=f2(cur_x)
print('minimum value of x is',min_val,"at","x=",cur_x)

#Plotting f(x)
X=np.arange(-1,2,0.01)
#y=F(X)
label_str = "$(x*(np.exp(x)-1)*(x-1)*((x-2)**2)*((x-3)**5))$"
plt.plot(X,F(X),label='label_str')
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'Q({cur_x:.4f},{min_val:.4f})',label='point minima')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.show()
#plt.savefig('/sdcard/mgowthami/optimization1/opt1/integ.pdf')
