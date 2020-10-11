
#import the necessary libraries
import matplotlib
import json
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams as params

#parse the json libraries!
with open('bettsredsox.json', 'r') as betts_redsox:
    sox = betts_redsox.read()
with open('bettsdodgers.json', 'r') as betts_dodgers:
    doyers = betts_dodgers.read()
redsox = json.loads(sox)
dodgers = json.loads(doyers)

# Extract Relevant Data
sabermetrics = {}
sabermetrics['BA'] = redsox['avg']
sabermetrics['OBP'] = redsox['obp']
sabermetrics['SLG'] = redsox['slg']
sabermetrics['OPS'] = redsox['obp']
sabermetrics['GO-FO'] = redsox['go_ao']
sabermetrics['BABIP'] = redsox['babip']

sabermetrics1 = {}
sabermetrics1['BA'] = dodgers['avg']
sabermetrics1['OBP'] = dodgers['obp']
sabermetrics1['SLG'] = dodgers['slg']
sabermetrics1['OPS'] = dodgers['obp']
sabermetrics1['GO-FO'] = dodgers['go_ao']
sabermetrics1['BABIP'] = dodgers['babip']

#creating a bar chart
width = 0.35
x = np.arange(len(sabermetrics.keys()))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, sabermetrics.values(), width, label='Red Sox',color='red')
rects2 = ax.bar(x + width/2, sabermetrics1.values(), width, label='Dodgers',color='blue')

#Labels/Title
ax.set_xlabel('Core Hitting Stat Categories')
ax.set_ylabel('Statistics')
ax.set_xticks(x)
ax.set_xticklabels(sabermetrics.keys())
ax.legend()
plt.title("Mookie Betts's Hitting Stats Between LA and Boston")
params['font.family'] = 'fantasy'

plt.show()

