import clusters

blogs,words,data=clusters.readfile('blogdata.txt') 
kclust=clusters.kcluster(data,k=5)
print([blogs[item] for item in kclust[0]])
print([blogs[item] for item in kclust[1]])
print([blogs[item] for item in kclust[2]])
print([blogs[item] for item in kclust[3]])
print([blogs[item] for item in kclust[4]])