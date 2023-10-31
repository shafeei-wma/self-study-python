# !pip install -q perfplot if not yet
# credit all code below to: @maximelabonne | https://mlabonne.github.io/blog/posts/2022-03-21-Efficiently_iterating_over_rows_in_a_Pandas_DataFrame.html

import pandas as pd
import perfplot 
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})

# Techniques
def forloop(df):
    total = []
    for index in range(len(df)):
        total.append(df['col1'].iloc[index] 
                   + df['col2'].iloc[index])
    return total

def itertuples(df):
    total = []
    for row in df.itertuples():
        total.append(row[1] + row[2])
    return total

def iterrows(df):
    total = []
    for index, row in df.iterrows():
        total.append(row['col1']
                   + row['col2'])
    return total

def apply(df):
    return df.apply(lambda row: row['col1']
                              + row['col2'], axis=1).to_list()

def comprehension(df):
    return [src + dst for src, dst in zip(df['col1'], df['col2'])]

def pd_vectorize(df):
    return (df['col1'] + df['col2']).to_list()

def np_vectorize(df):
    return (df['col1'].to_numpy() + df['col2'].to_numpy()).tolist()

# Perfplot
functions = [iterrows, forloop, apply, itertuples,
             comprehension, pd_vectorize, np_vectorize]
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

out = perfplot.bench(
      setup=lambda n: pd.concat([df]*n, ignore_index=True),
      kernels=functions,
      labels=[str(f.__name__) for f in functions],
      n_range=[2**n for n in range(20)],
      xlabel='Number of rows',
)

plt.figure(figsize=(14,8))
out.show()