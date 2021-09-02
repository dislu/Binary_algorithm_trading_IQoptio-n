''' Problem:
    Binary option trading is a type of trading in which traders have to predict the result of a yes/no situation by the end of a determined period, and
    the payoff is either a fixed amount of money as compensation or nothing else.Trading on 1-minute Binary options, a binary trader want to minimize his 
    loss, if the algorithms he build runs into losses. He build following two algoriths:
    Algorith One: For the very first bet, he bets on 'UP' option, and in the next bet, he bets on 'DOWN' option. He follow the strategy of changing the bet 
                  option on every next step.
    Algorithm Two: In this algorithm, he follow the same strategy as in the first algorithm, but start with 'DOWN' option.
    Let initial bet amount are x[0], x[1] in algorthm one and two respectively.In both the strategy, if he lose, he multiply the bet amount by x[3]>0., and 
    if he wins, he multiply the bet amount by x[2]>0.
    Study of algoriths for first two step:
    Suppose, the trader gets 90% return on his investment, if he wins else he loses his investment.There are four possible cases.
    case 1: 'UP' 'UP'
           Algorithm One: Profit in first step and loss in the second step
           Algorithm Two: Loss in the first step and profit in the second step
           total profit = x[0]*0.9 (algo1 first step) + x[2]*0.9*x[1] (algo2 second step)
           total loss   = x[1] (algo2 first step) + x[2] *x[0] (algo1 second step)
           equation:
                    total profit > total loss
                    0.9*(x[0] + x[2]*x[1]) > x[1] + x[2]*x[0] 
    case 2: 'DOWN' 'DOWN'
           Algorithm One: Loss in first step and profit in the second step
           Algorithm Two: Profit in the first step and loss in the second step
           total profit = x[1]*0.9 (algo2 first step) + x[3]*0.9*x[0] (algo1 second step)
           total loss   = x[0] (algo1 first step) + x[3]*x[1] (algo2 second step)
           equation:
                    total profit > total loss
                    0.9*(x[1] + x[3]*x[0]) > x[0] + x[3]*x[1]
    case 3: 'UP' 'DOWN'
           Algorithm One: Profit in first step and profit in the second step
           Algorithm Two: Loss in the first step and loss in the second step
           total profit = x[0]*0.9 (algo1 first step) + x[3]*0.9*x[0] (algo1 second step)
           total loss   = x[1] (algo2 first step) + x[2]*x[1] (algo2 second step)
           equation:
                    total profit > total loss
                    0.9*(x[0] + x[3]*x[0]) > x[1] + x[2]*x[1]
    case 4: 'DOWN' 'UP'
           Algorithm One: Loss in first step and loss in the second step
           Algorithm Two: Profit in the first step and profit in the second step
           total profit = x[1]*0.9 (algo2 first step) + x[3]*0.9*x[1] (algo2 second step)
           total loss   = x[0] (algo2 first step) + x[2]*x[0] (algo1 second step)
           equation:
                    profit = 0.9*(x[1] + x[3]*x[1]) , loss =  x[0] + x[2]*x[1]
                    Objective function = 0.9*(x[1] + x[3]*x[1]) - x[0] + x[2]*x[1]
    Third and fourth cases are similar and analysis of the problem says that the trader have to bear loss either in third or fourth case. Here, trader chose to 
    bear loss in the fourth case.The aim of the program is to find optimum values of x[0]--x[3], so that objective function in 'case 4' is minimized'''
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
