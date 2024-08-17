import pandas as pd
from scipy.stats import wilcoxon

a = pd.read_table('time.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))
print(wilcoxon(a['a1'], a['a2'], correction=True))


a = pd.read_table('retrieval_time.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))
print(wilcoxon(a['a1'], a['a2'], correction=True))

a = pd.read_table('nasa-tlx.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))
print(wilcoxon(a['a1'], a['a2'], correction=True))