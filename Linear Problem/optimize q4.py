from scipy.optimize import minimize

def objective_function(x):
    return 250*x[0]+300*x[1]+600*x[2]+50*x[3]

def constraint1(x):
    return 100*x[0]+0*x[1]+11*x[2]+18*x[3]-700

def constraint2(x):
    return 5*x[0]+58*x[1]+0*x[2]+5*x[3]-400

def constraint3(x):
    return 3*x[0]+6*x[1]+20*x[2]+2*x[3]-50

def constraint4(x):
    return 70*x[0]+350*x[1]+420*x[2]+30*x[3]-2500

bounds = [(0, 100), (0, 100), (0, 100), (0, 100)]


constraints = [{'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3},
               {'type': 'ineq', 'fun': constraint4}]


x0=[0,0,0,0]
result = minimize(objective_function, x0, bounds=bounds, constraints=constraints)
x=result.x.round(0)
cost=objective_function(x)

print(x)
print(cost)
