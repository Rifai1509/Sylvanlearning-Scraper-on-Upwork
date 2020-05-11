import json
import pandas as pd
with open('data.json', 'r') as file:
    data = file.read()
datas = json.loads(data)

df = pd.DataFrame(datas)
# print(df)
df.to_excel('sample.xlsx', index=False)