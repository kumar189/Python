# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:27:43 2017

@author: MANI
"""
#imports all the libraries and packages required
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as p
#loads the data in as raw_data
raw_data = p.read_csv('Customers.csv')
#loads the required values in file columns 2 and 4 into X
X = raw_data.iloc[:, [3, 4]].values
#Uses function KMeans to generate 5 clusters with random_state 42
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
#plot all the clusters with respective colors on to a graph
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
#plot the cluster centers with a specified color
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers data')
plt.xlabel('')
plt.ylabel('')
plt.legend()
plt.show()
