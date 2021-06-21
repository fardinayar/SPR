import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('doughs.dat', sep='\s', engine='python')
X = data.drop(['Index','Restaurant'],axis=1)
y = data['Restaurant'].replace({1:1,2:1,3:1,4:1,5:2,6:2}).values

def pca(X,n):
    mean = X.mean()
    Z = X-mean
    S = np.cov(Z.T) * (len(X.index)-1)
    eigenValues, eigenVectors = np.linalg.eig(S)
    idx = eigenValues.argsort()[::-1]   
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]  
    print(eigenValues)
    return eigenVectors[:n,:],Z

pcs,Z = pca(X,3)
t_X = (pcs.dot(Z.T)).T

plt.scatter(t_X[:,0],t_X[:,1],c=y,label=y)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(t_X[:,0], t_X[:,1],t_X[:,2], c = y, marker='o',label=y)
plt.show()

