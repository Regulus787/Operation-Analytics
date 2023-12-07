import pandas as pd
from pulp import *
import numpy as np

demands_df = pd.read_csv('D:\Programming\School\Operation Analytics\Assigment\caseStudy_dem.csv')
supplies_df = pd.read_csv('D:\Programming\School\Operation Analytics\Assigment\caseStudy_sup.csv')

def distance(x1,x2,y1,y2):
    distance=((x1-x2)**2+(y1-y2)**2)**(1/2)
    return distance

def cover(x):
    if x<=30000:
        return 1
    else:
        return 0

demands=demands_df['demand']
number_of_hospital=5

model=LpProblem("Maximal covering Problem",LpMaximize)
setup = [LpVariable(name=f"x{a}", lowBound=0, cat="Binary") for a in range(supplies_df.shape[0])]
values=[]

for i, supply in supplies_df.iterrows():
    results = []
    for j, demand in demands_df.iterrows():
        dist = distance(demand['x'], supply['x'], demand['y'], supply['y'])
        cov = cover(dist)
        results.append(cov)
    results = np.array(results)
    covdemand = lpSum(results * demands)
    values.append(covdemand)
values = np.array(values)
objective_function = lpSum(values*setup)
model += objective_function
model += sum(setup) == number_of_hospital
model.solve()
for variable in setup:
    print(f"{variable.name} = {variable.varValue}")
print(objective_function.value())