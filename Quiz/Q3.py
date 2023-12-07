from pulp import *

model = LpProblem('portfolio', LpMaximize)
x1=LpVariable('A',lowBound=0, upBound=1)
x2=LpVariable('B', lowBound=0,upBound=1)
x3=LpVariable('C', lowBound=0,upBound=1)
x4=LpVariable('D', lowBound=0,upBound=0.1)
x5=LpVariable('E', lowBound=0,upBound=0.3)

objective_function=0.08*x1+0.1*x2+0.11*x3+0.12*x4+0.09*x5

model+=objective_function
model+=x1+x2+x3+x4+x5==1,"Constraints"
model+=1/2*(-1*x1+x2+x3)<=0,"Constraints2"
model+=x3+x4-x5<=0,"Constraints3"
print(model)
model.solve()
print(x1.value())
print(x2.value())
print(x3.value())
print(x4.value())
print(x5.value())
