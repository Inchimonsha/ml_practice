import pandas_cl as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

data=pd.read_csv(r"C:\main\lang\python\test\datasets\USArrests.csv",index_col=0)
data=data.dropna()
data.head()

kmeans=KMeans(n_clusters=4)
kmeans_model=kmeans.fit(data)
k_values=kmeans_model.labels_

plt.figure(figsize=(15,7))
plt.scatter(data.iloc[:,0],data.iloc[:,1],c=k_values,cmap="viridis")
centers=kmeans_model.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c="black",s=200,alpha=0.5)

plt.show()

