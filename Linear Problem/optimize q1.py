from scipy.optimize import minimize

def objective_function(x):
    return 200*x[0]+50*x[1]

def constraint1(x):
    return 0.8*0.3*x[0]+0.25*0.55*x[1]-350

def constraint2(x):
    return 0.8*0.5*x[0]+0.25*0.35*x[1]-450

def constraint3(x):
    return 0.8*0.2*x[0]+0.25*0.1*x[1]-200

def constraint4(x):
    return 0.2*x[0]+0.75*x[1]


bounds = [(0, 10000), (0, 10000)]


constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3},
               {'type': 'ineq', 'fun': constraint4}]


x0=[0,0]
result = minimize(objective_function, x0, bounds=bounds, constraints=constraints)
x=result.x.round(0)
cost=objective_function(x)
print(x)
print(cost)