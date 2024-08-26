import pandas as pd
from scipy.stats import wilcoxon

a = pd.read_table('./data/ui_time.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))


a = pd.read_table('./data/retrieval_time.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))


a = pd.read_table('./data/nasa-tlx.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))


a = pd.read_table('./data/retrieval_time_noassist.tsv')
print(wilcoxon(a['a1'], a['a2'], mode='exact', alternative='two-sided', zero_method='wilcox'))