import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('plotText.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
plt.plot(11,98,marker='*', color='red',markersize=12)
plt.plot(52,431,marker='*', color='red',markersize=12)
plt.plot(63,536,marker='*', color='red',markersize=12)
plt.plot(65,542,marker='*', color='red',markersize=12)
plt.annotate('Dr. Nwala\'s Friends : 98' , xy=(17, 98))
plt.annotate('Median : 431' , xy=(40, 500))
plt.annotate('Standard Deviation : 536' , xy=(63, 350),)
plt.annotate('Mean : 542' , xy=(65, 700))
plt.xlim(0, 105)
plt.xlabel('All Friends')
plt.ylabel('No. of Friends for Each Friend')
plt.title('Facebook Friends Vs Each Friend count')
plt.legend()
plt.show()