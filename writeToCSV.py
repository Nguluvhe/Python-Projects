import pandas as pd

data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data)

df.to_csv('my_data.csv', index=False)