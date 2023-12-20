import pandas as pd

# csv1_name=input()
# csv2_name=input()
csv1_name = "registration_11_29.csv"
csv2_name = "results_11_29.csv"
csv1_str = pd.read_csv(csv1_name)
csv2_str = pd.read_csv(csv2_name)
# csv1_str=pd.read_csv(csv1_name,sep=",",skiprows=1,header=0)
# csv2_str=pd.read_csv(csv2_name,sep=",",skiprows=1,header=0)
csv1_df = pd.DataFrame(csv1_str)
csv2_df = pd.DataFrame(csv2_str)
df = pd.DataFrame(pd.merge(csv1_df, csv2_df, on="ID"))
df.sort_values(by="ID")
name_final1 = df.loc[df["WBC"] < 3.5]
name_final2 = df.loc[df["WBC"] > 9.5]
name_final = pd.merge(name_final1, name_final2, how="outer")
names = list(name_final.iloc[:, 1].values)
print("Patients with abnormal WBC results include: ", end="")
for i in range(len(names)):
    print(names[i], end=" ")
