import numpy as np
from scipy.optimize import minimize

def objective(x):
    return -(x[0]+x[0]*x[3])+0.9*(x[1]+x[1]*x[2])

def constraint1(x):
    return 0.9*(x[0]+x[1]*x[3])-(x[0]*x[2]+x[1])

def constraint2(x):
    return 0.9*(x[0]*x[3]+x[1])-(x[0]+x[1]*x[2])

def constraint3(x):
    return 0.9*(x[0]+x[2]*x[0])-(x[1]+x[1]*x[3])

# initial guesses
n = 4
x0 = np.zeros(n)
x0[0] = 3.0
x0[1] = 2.0
x0[2] = 1.7
x0[3] = 0.5

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# optimize
a = (3.0,20.0) 
b = (2.0,15.0)
c = (0,1)
d = (1,5)
bnds = (a, b, c, d)
con1 = {'type': 'ineq', 'fun': constraint1} 
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': contsraint3}
cons = ([con1,con2,con3])
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
print('x4 = ' + str(x[3]))