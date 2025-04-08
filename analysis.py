import pandas as pd

data = pd.read_csv('TypeMetrics.csv')

data['average'] = data[['LCOM1', 'LCOM2', 'LCOM3', 'LCOM4', 'LCOM5', 'YALCOM']].mean(axis=1)
data = data.sort_values(by='average', ascending=False, ignore_index=True).head()

print(data)

data.to_csv('TypeMetrics_sorted.csv', index=False)