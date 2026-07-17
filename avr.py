import pandas as pd
data={"Name":["paul","raj",None,"Reena"],
      "mark":[25,None,22,21]}
df=pd.DataFrame(data)
print(df)
print("missing values")
print(df.isnull())
print("null values")
print(df.isnull().sum())