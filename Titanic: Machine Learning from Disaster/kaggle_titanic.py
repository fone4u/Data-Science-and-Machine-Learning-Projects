import pandas as pd 

df = pd.read_csv('/home/shubham/Documents/Kaggle/Titanic/train.csv')
df = df.drop(['Ticket', 'Cabin'], axis = 1)
print df