from pulp import *

model = LpProblem('production_problem', LpMinimize)
x1=LpVariable('빵',lowBound=0)
x2=LpVariable('고기', lowBound=0.2)
x3=LpVariable('감자', lowBound=0)
x4=LpVariable('배추', lowBound=0)
x5=LpVariable('우유', lowBound=0.2)
x6=LpVariable('젤라틴', lowBound=0)

objective_function=1500*x1+5000*x2+400*x3+320*x4+920*x5+1900*x6

model+=objective_function
model+=25000*x1+2900*x2+630*x3+95*x4+630*x5+3400*x6>=3000,"Constraints"
model+=79*x1+149*x2+16*x3+8*x4+32*x5+86*x6>=70,"Constraints2"
model+=830*x1+84*x2+86*x3+279*x4+1060*x5+0*x6>=800,"Constraints3"
model+=0*x1+0*x2+140*x3+1690*x4+1430*x5+0*x6>=5,"Constraints4"

print(model)
model.solve()
print(x1.value())
print(x2.value())
print(x3.value())
print(x4.value())
print(x5.value())
print(x6.value())