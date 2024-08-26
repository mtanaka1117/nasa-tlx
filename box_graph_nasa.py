import pandas as pd
import matplotlib.pyplot as plt

scales = ['Mental Demand', 'Physical Demand', 'Temporal Demand', 'Performance', 'Effort', 'Frustration']

data = pd.read_table('./data/nasa.tsv', sep='\t')

data_proposed = []
data_compared = []

for scale in scales:
    scale_data = data[data['Scale'] == scale]
    data_proposed.append(scale_data['Proposed System'])
    data_compared.append(scale_data['Compared System'])


combined_data = []
labels = []
positions = []
offset = 0.5  # 同じスケールのボックス間の間隔
colors = ['lightcoral', 'cornflowerblue']

for i in range(len(scales)):
    combined_data.append(data_proposed[i])
    combined_data.append(data_compared[i])
    labels.append(f'{scales[i]} - Proposed')
    labels.append(f'{scales[i]} - Compared')
    positions.append(i * 2)
    positions.append(i * 2 + offset)
    


fig, ax = plt.subplots()
boxplot = ax.boxplot(combined_data, positions=positions, patch_artist=True, widths=0.4, showmeans=True)
    
for mean in boxplot['means']:
    mean.set_marker('x')
    mean.set_markerfacecolor('black')
    mean.set_markeredgecolor('black')

for patch, color, median, flier, in zip(boxplot['boxes'], colors * len(scales), boxplot['medians'], boxplot['fliers']):
    patch.set_facecolor(color)
    median.set_color('black')
    flier.set(marker='o', markerfacecolor=color, alpha=0.8)
    

ax = plt.gca()
ax.set_title('Results of NASA-TLX')
ax.set_ylabel('Score')

xticks = [i * 2 + offset / 2 for i in range(len(scales))]
ax.set_xticks(xticks)
ax.set_xticklabels(scales)
ax.tick_params(axis='y', labelsize=12) 

custom_lines = [plt.Line2D([0], [0], color='lightcoral', lw=4),
                plt.Line2D([0], [0], color='cornflowerblue', lw=4)]
ax.legend(custom_lines, ['Proposed System', 'Compared System'], loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

plt.grid(axis='y', color='lightgray')
plt.tight_layout()
plt.show()