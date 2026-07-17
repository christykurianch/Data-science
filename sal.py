import pandas as pd
data={"dept":["mca","cse","mca","ECE"],
      "empname":["abc","def","ghi","jkl"],
      "salary":[150000,45000,60000,45000]}
df=pd.DataFrame(data)
print(df)
print("Average salary of each department")
avg=df.groupby("dept")["salary"].mean()
print(avg)