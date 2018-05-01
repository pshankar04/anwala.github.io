import clusters
import numpredict
def findNearestNeighbour(i, data, k):
    testing = data[i]
    neighbors = numpredict.knnestimate(data, testing, k)
    for i in neighbors:
        print(blogs[i[1]])


blogs, text, data = clusters.readfile("blogDataForknn.txt")
for name in "F-Measure", "Web Science and Digital Libraries Research Group":
    for k in 1, 2, 5, 10, 20:
        print("Blog Name", name)
        print("For K", k)
        findNearestNeighbour(blogs.index(name), data, k)
        print("\n\n")