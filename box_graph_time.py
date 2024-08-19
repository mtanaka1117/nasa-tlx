import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def milliseconds_to_time(ms):
    minutes = int(ms // 60000)
    seconds = int((ms % 60000) / 1000)
    return f'{minutes:02}:{seconds:02}'

def format_func(value, tick_number):
    return milliseconds_to_time(value)


data = pd.read_table('retrieval_time_clock.tsv', sep='\t')

fig, ax = plt.subplots()
boxplot = ax.boxplot([data['Proposed System'], data['Compared System']], 
                    positions=[0.3, 1],
                    patch_artist=True,
                    showmeans=True)

colors = ['lightcoral', 'cornflowerblue']

for patch, median, flier, color in zip(boxplot['boxes'], boxplot['medians'], boxplot['fliers'], colors):
    patch.set_facecolor(color)
    median.set_color('black')
    flier.set(marker='o', markerfacecolor=color, alpha=0.8)
    
for mean in boxplot['means']:
    mean.set_marker('x')
    mean.set_markerfacecolor('black')
    mean.set_markeredgecolor('black')

ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
# ax.set_title('Object Searching Time on UI', size=18)
ax.set_title('Object Retrieval Time', size=18)
ax.set_ylabel('Time', size=14)
ax.set_xticklabels(labels=['Proposed System', 'Compared System'], fontsize=14)
ax.tick_params(axis='y', labelsize=12) 

plt.grid(axis='y', color='lightgray')

plt.show()