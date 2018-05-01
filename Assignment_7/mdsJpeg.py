import clusters

blog,words,data=clusters.readfile('blogdata.txt') 
coords=clusters.scaledown(data)
clusters.draw2d(coords,blog,jpeg='blogsMDS.jpg')

