from pulp import *
model=LpProblem(name="Portfolio", sense=LpMaximize)

num_vars=5
var_x=[LpVariable(name=f"x{i}", lowBound=0, cat ="Binary") for i in range(1, num_vars+1)] # x1 to x5

num_constr_1=1
constr_1=[]
constr_1_coeffs=[6000, 4000, 8000, 5000, 7000]
for i in range(num_constr_1):
    rhs_values=[20000]
    constraint=LpConstraint(
        e=LpAffineExpression([(var_x[j], constr_1_coeffs[j]) for j in range(num_vars)]),
        sense=LpConstraintLE,
        rhs=rhs_values[i],
        name=f"constraint_{i+1}"
    )
    constr_1.append(constraint)

obj_coefficients=[160, 200, 300, 500, 900]
objective=LpAffineExpression([(var_x[j], obj_coefficients[j]) for j in range(num_vars)])
model+=objective

for constraint in constr_1:
    model+=constraint

print(model)
model.writeLP('out.txt')

model.solve()

for variable in var_x:
    print(f"{variable.name}: {variable.value()}")

print(f"Optimal objective value: {model.objective.value()}")

