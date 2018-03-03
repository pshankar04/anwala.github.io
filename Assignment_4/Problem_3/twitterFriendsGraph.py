import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('twitterFriends-Friends.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
plt.plot(10,74,marker='*', color='red',markersize=12)
plt.plot(40,503,marker='*', color='red',markersize=12)
plt.plot(56,1057,marker='*', color='red',markersize=12)
plt.plot(61,1555,marker='*', color='red',markersize=12)
plt.annotate('Dr. Nwala\'s Friends : 74' , xy=(12, 50))
plt.annotate('Median : 503' , xy=(42, 497))
plt.annotate('Standard \n Deviation : 1555' , xy=(63, 1510),)
plt.annotate('Mean : 1057' , xy=(61, 1050))
plt.ylim(0, 2000)
plt.xlim(0, 80)
plt.xlabel('All Friends')
plt.ylabel('No. of Friends for Each Friend')
plt.title('Twitter Friends Vs Each Friend count')
plt.legend()
plt.show()