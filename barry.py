#import libraries
import json
import matplotlib
from matplotlib import pyplot as plt

#parse json file
with open('barry.json', 'r') as i:
    j = i.read()
barry = json.loads(j)

#create a list of viewers in millions
viewers_millions = []
for ratings in barry:
    viewers_millions.append(ratings["viewers_millions"])
print('viewers: ',viewers_millions)

#dates of aired episodes
labels = '03/13/19','04/07/19','04/14/19','04/21/19','04/28/19','05/05/19'

#exploding piece of the pie chart
explode = (0,0,0,0,0.1,0)

#creating the pie chart
fig1,ax1 = plt.subplots()
ax1.pie(viewers_millions,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.title('Barry Episodes from 3/13 - 5/5 Based on Viewership (millions)')

plt.show()

#print(json.dumps(barry,indent=2,sort_keys=True))



