import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
import sys

#Dylan Chu
#5/18/16
#CMSC471
#Project 4
#K-Means Clustering

#reads file into graph
def readFile(infile):
    testlist = []
    f=open(infile,"r")
    for line in f:
        x, y = line.split()
        testlist.append([x,y])
    f.close()
    return testlist

#takes the command line args
def processCommandLineArgs():
    numClusters = sys.argv[1]
    infile = sys.argv[2]

    return numClusters, infile

#does kmeans clustering
#points is the given dataset
#clusters is the number of clusters
#function will show the points on a graph
def kcluster(points, clusters):
    #normalize the data points
    data = whiten(points)
    centroids,_ = kmeans(data,clusters)
    idx,_ = vq(data,centroids)

    colors = ['ob','or','oy','og','oc','om','ok']
    for i in range(clusters):
        j=i
        if i >=(len(colors)):
            j=i-len(colors)

        plt.plot(data[idx==i,0],data[idx==i,1],colors[j])
        
    plt.plot(centroids[:,0],centroids[:,1],'sg',markersize=10)
    plt.show()
    

def main():
    clusters, infile = processCommandLineArgs()  
    points = readFile(infile)
    
    #these comments are left in for debugging purpose
    #points = np.random.rand(200,2)
    #clusters = 3
    
    
    kcluster(points, clusters)

    

main()

