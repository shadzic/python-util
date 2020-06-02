import pandas as pd
data = pd.read_csv('data.csv')
data.head()
data.describe()
data.info()

# with plots:
import pandas_profiling
pandas_profiling.ProfileReport(data)
