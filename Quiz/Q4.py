from pulp import *

model = LpProblem('optimiztion', LpMaximize)
x1=LpVariable('A',lowBound=0)
x2=LpVariable('B', lowBound=0)

objective_function=3*x1+5*x2

model+=objective_function
model+=x1<=4,"Constraints1"
model+=x2<=6,"Constraints2"
model+=3*x1+2*x2<=18,"Constraints3"


print(model)
model.solve()
print(x1.value())
print(x2.value()) 