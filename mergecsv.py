import pandas as pd
import glob

files = glob.glob('./CSE141FA17CSV/*.csv')
print files

df = pd.read_csv(files[0])
for f in files[1:]:
    dftemp = pd.read_csv(f)
    df = df.merge(dftemp, how='outer')

df.to_csv('CSE141FA17.csv')
