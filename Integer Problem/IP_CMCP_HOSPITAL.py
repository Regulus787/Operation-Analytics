import pulp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

event_locations=pd.read_csv('data/caseStudy_dem.csv')[['x','y']]
hospital_candidate_locations=pd.read_csv('data/caseStudy_sup.csv')
expected_patients=pd.read_csv('data/caseStudy_dem.csv')['demand']

num_events=event_locations.shape[0]
num_hospital_candidates=hospital_candidate_locations.shape[0]
num_hospitals_to_select=5
hospital_capacity=3000
hospital_radius_m=30000


distances=np.zeros((num_events,num_hospital_candidates))
for i in range(num_events):
    for j in range(num_hospital_candidates):
        dx=event_locations['x'][i]-hospital_candidate_locations['x'][j]
        dy=event_locations['y'][i]-hospital_candidate_locations['y'][j]
        distances[i,j]=np.sqrt(dx**2 + dy**2)
within_radius=distances<=hospital_radius_m

problem=pulp.LpProblem("HospitalLocation",pulp.LpMaximize)

hospital_vars=pulp.LpVariable.dicts("Hospital",range(num_hospital_candidates),cat='Binary')
serve_vars=pulp.LpVariable.dicts("Serve",(range(num_events),range(num_hospital_candidates)),lowBound=0,upBound=1,cat='Continuous')

problem+=pulp.lpSum(expected_patients[i] * serve_vars[i][j] for i in range(num_events) for j in range(num_hospital_candidates) if within_radius[i, j])

problem+=pulp.lpSum(hospital_vars[j] for j in range(num_hospital_candidates))==num_hospitals_to_select

for i in range(num_events):
    for j in range(num_hospital_candidates):
        problem += serve_vars[i][j] <= hospital_vars[j]

for j in range(num_hospital_candidates):
    problem += pulp.lpSum(expected_patients[i] * serve_vars[i][j] for i in range(num_events) if within_radius[i, j]) <= hospital_capacity * hospital_vars[j]

for i in range(num_events):
    problem += pulp.lpSum(serve_vars[i][j] for j in range(num_hospital_candidates) if within_radius[i, j]) <= 1.0

problem.solve()

for variable in hospital_vars.values():
    print(f"{variable.name} = {variable.varValue}")


total_patients=0
for i in range(num_events):
    total_patients+=expected_patients[i]

print(f"총 환자 수 : {total_patients}")
print(f"이송 성공한 총 환자 수 : ",problem.objective.value())

hospital_solution=[v for v in problem.variables() if v.varValue>0 and v.name.startswith('Hospital')]
incident_solution=[v for v in problem.variables() if v.varValue>0 and v.name.startswith('Serve')]

hospital_indices=[int(v.name.split('_')[1]) for v in hospital_solution]

incident_assignments=[(int(v.name.split('_')[1]), int(v.name.split('_')[2])) for v in incident_solution]

np_event=np.array(event_locations)
plt.scatter(np_event[:, 0], np_event[:, 1], c='blue', label='Incident points')

np_hospital=np.array(hospital_candidate_locations)
plt.scatter(np_hospital[:, 0], np_hospital[:, 1], c='red', label='All hospital candidates')
plt.scatter(np_hospital[hospital_indices, 0], np_hospital[hospital_indices, 1], c='green', label='Selected hospitals')

for i, j in incident_assignments:
    plt.plot([np_event[i, 0], np_hospital[j, 0]], [np_event[i, 1], np_hospital[j, 1]], 'k-', lw=0.1)

plt.title('Hospital Location Optimization')
plt.legend()
plt.show()