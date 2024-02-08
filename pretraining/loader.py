import numpy as np
import pandas as pd
import secrets
import warnings
from datetime import datetime
warnings.filterwarnings("ignore")



# make y column with 1 for existing entries
df = pd.read_csv("dataset_42.csv", sep=",") 
print(len(df))

print(df)
df.to_csv('out.csv', index=True)