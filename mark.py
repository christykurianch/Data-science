import pandas as pd
data={"Name":["parvathy","Reena","neenu","Anu","Amalu"],
      "marks":[89,90,95,66,95]}
df=pd.DataFrame(data)
result=df[df["marks"]>80].sort_values(by="marks",ascending=False)
print(result)