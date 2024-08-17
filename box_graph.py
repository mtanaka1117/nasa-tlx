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
ax.boxplot([data['Proposed System'], data['Compared System']], 
           labels=['Proposed System', 'Compared System'], 
           positions=[0.5, 1])


ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
ax.set_title('Object Retrieval Time')
ax.set_ylabel('Time')

plt.show()