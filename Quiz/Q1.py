from pulp import *

model = LpProblem('production_problem', LpMaximize)
x=LpVariable('desk',lowBound=0)
y=LpVariable('chair', lowBound=0)
objective_function=20000*x+50000*y

model+=objective_function
model+=0.1*x+0.4*y<=50,"Constraints"
model+=4*x+8*y<=1200,"Constraints2"

print(model)
model.solve()
print(x.value())
print(y.value())