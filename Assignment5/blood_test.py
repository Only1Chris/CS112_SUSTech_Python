import pandas as pd

# reg_file=input()
# res_file=input()
reg_file = "registration_11_29.csv"
res_file = "results_11_29.csv"

reg = pd.read_csv(reg_file)
res = pd.read_csv(res_file)
result = pd.merge(reg, res, how='inner', on='ID')
name=result.loc[(result['WBC'] < 3.5) | (result['WBC'] >9.5)]['name']
# name = pd.concat([result[result['WBC'] < 3.5], result[result['WBC'] > 9.5]],axis=0)['name']  # 这种方式也可以，但是更复杂

print("Patients with abnormal WBC results include: " + " ".join(name))
