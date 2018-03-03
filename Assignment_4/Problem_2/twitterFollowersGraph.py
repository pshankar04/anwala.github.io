import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('twitterFollowers-Friends.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
plt.plot(55,194,marker='*', color='red',markersize=12)
plt.plot(99,551,marker='*', color='red',markersize=12)
plt.plot(163,2321,marker='*', color='red',markersize=12)
plt.plot(191,8601.97,marker='*', color='red',markersize=12)
plt.annotate('Dr. Nwala\'s Followers : 194' , xy=(10, 380))
plt.annotate('Median : 551' , xy=(80, 900))
plt.annotate('Mean : 2321' , xy=(168, 2321),)
plt.annotate('Standard\nDeviation : 8601.97' , xy=(140, 8300))
plt.xlim(0, 200)
plt.ylim(0, 9000)
plt.xlabel('All Followers')
plt.ylabel('No. of Friends for Each Follower')
plt.title('Twitter Followers Vs Each Follower\'s Friend count')
plt.legend()
plt.show()