from pulp import *
model=LpProblem(name="Maximal covering problem", sense=LpMaximize)

num_vars=6
var_x=[LpVariable(name=f"x{i}", lowBound=0, cat="Binary") for i in range(1, num_vars + 1)]  # x1 to x6
var_y=[LpVariable(name=f"y{i}", lowBound=0, cat="Binary") for i in range(1, num_vars + 1)]  # y1 to y6

num_constr_1=6
constr_1=[]
constr_1_coeffs=[[1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1],
                   [0, 0, 0, 1, 1, 1]]
for i in range(num_constr_1):
    rhs_values=[0, 0, 0, 0, 0, 0]
    constraint=LpConstraint(
        e=LpAffineExpression([(var_y[j], constr_1_coeffs[i][j]) for j in range(num_vars)] + [(var_x[i], -1)]),
        sense=LpConstraintGE,
        rhs=rhs_values[i],
        name=f"constraint_{i + 1}"
    )
    constr_1.append(constraint)

num_constr_2=1
constr_2=[]
constr_2_coeffs=[1, 1, 1, 1, 1, 1]
for i in range(num_constr_2):
    rhs_values=[3]
    constraint=LpConstraint(
        e=LpAffineExpression([(var_y[j], constr_2_coeffs[j]) for j in range(num_vars)]),
        sense=LpConstraintLE,
        rhs=rhs_values[i],
        name=f"constraint_{num_constr_1 + i + 1}"
    )
    constr_2.append(constraint)

obj_coefficients=[1500, 2000, 1700, 2010, 1300, 1000]
objective = LpAffineExpression([(var_x[j], obj_coefficients[j]) for j in range(num_vars)])
model += objective

for constraint in constr_1 + constr_2:
    model+=constraint
print(model)
model.writeLP('out.txt')

model.solve()

for variable in var_x:
    print(f"{variable.name}: {variable.value()}")

for variable in var_y:
    print(f"{variable.name}: {variable.value()}")

print(f"Optimal objective value: {model.objective.value()}")