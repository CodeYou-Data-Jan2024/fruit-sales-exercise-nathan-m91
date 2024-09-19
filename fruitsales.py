import pandas as pd
fruits_sales = {'Apples' : [35, 41], 'Bananas' : [21, 34]}
df = pd.DataFrame(fruits_sales, index= ['2017 Sales', '2018 Sales'])
print(df)
df.to_csv('fruits_sales.csv')
