from scipy.optimize import minimize
import numpy as np
def objective_function(x):
    return np.sum(x)

def constraint1(x):
    return x[0]+x[3]+x[4]+x[5]+x[6]+x[7]-7

def constraint2(x):
    return x[1]+x[4]+x[5]+x[6]+x[7]+x[0]-11

def constraint3(x):
    return x[2]+x[5]+x[6]+x[7]+x[0]+x[1]-10

def constraint4(x):
    return x[3]+x[6]+x[7]+x[0]+x[1]+x[2]-9

def constraint5(x):
    return x[4]+x[7]+x[0]+x[1]+x[2]+x[3]-14

def constraint6(x):
    return x[5]+x[0]+x[1]+x[2]+x[3]+x[4]-13

def constraint7(x):
    return x[6]+x[1]+x[2]+x[3]+x[4]+x[5]-9

def constraint8(x):
    return x[7]+x[2]+x[3]+x[4]+x[5]+x[6]-8

bounds = [(0, 10000)]*8


constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3},
               {'type': 'ineq', 'fun': constraint4},
               {'type': 'ineq', 'fun': constraint5},
               {'type': 'ineq', 'fun': constraint6},
               {'type': 'ineq', 'fun': constraint7},
               {'type': 'ineq', 'fun': constraint8}]

x0=[0]*8
result = minimize(objective_function, x0, bounds=bounds, constraints=constraints)
x=result.x.round(0)
people=objective_function(x)
print(x)
print(int(people),"명")