from scipy.optimize import minimize
import numpy as np
import pandas as pd

def objective_function(x):
    return np.sum(cost*x)

def constraint1(x):
    sum=0
    for i in range(0,4):
        i=i*5
        sum=sum+x[i]
    return sum-15

def constraint2(x):
    sum=0
    for i in range(0,4):
        i=i*5+1
        sum=sum+x[i]
    return sum-8

def constraint3(x):
    sum=0
    for i in range(0,4):
        i=i*5+2
        sum=sum+x[i]
    return sum-7

def constraint4(x):
    sum=0
    for i in range(0,4):
        i=i*5+3
        sum=sum+x[i]
    return sum-4

def constraint5(x):
    sum=0
    for i in range(0,4):
        i=i*5+4
        sum=sum+x[i]
    return sum-8

def constraint6(x):
    sum=0
    for i in range(-1,4):
        i=i+1
        sum=sum+x[i]
    return -1*(sum-14)

def constraint7(x):
    sum=0
    for i in range(4,9):
        sum=sum+x[i]
    return -1*(sum-10)

def constraint8(x):
    sum=0
    for i in range(9,14):
        i=i+1
        sum=sum+x[i]
    return -1*(sum-7)

def constraint9(x):
    sum=0
    for i in range(14,19):
        i=i+1
        sum=sum+x[i]
    return -1*(sum-15)

cost=pd.read_excel("cost.xlsx")
cost=np.array(cost)
cost=np.delete(cost,0,axis=1)
cost=cost.reshape(1,-1)
bounds = [(0, 10000)]*20
x0=np.zeros(20)

constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3},
               {'type': 'ineq', 'fun': constraint4},
               {'type': 'ineq', 'fun': constraint5},
               {'type': 'ineq', 'fun': constraint6},
               {'type': 'ineq', 'fun': constraint7},
               {'type': 'ineq', 'fun': constraint8},
               {'type': 'ineq', 'fun': constraint9}]


result = minimize(objective_function, x0, bounds=bounds, constraints=constraints)
x=result.x
total_cost=objective_function(x)
ecost=np.sum(x*cost)
print(result)
print(total_cost)
