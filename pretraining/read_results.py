import numpy as np
import pandas as pd


f = "mlm_train.csv"
print (f)
results = pd.read_csv(f)
sampson = results.sample(n=130471)
sampson = sampson.filter(['Peptide', 'CDR3b'])


d42 = pd.read_csv("mlm_train_42.csv")
d42 = d42.filter(['Peptide', 'CDR3b'])
d42=d42.append(sampson)
df = d42.reset_index()
print(df)

df.to_csv('out.csv', index=True)
