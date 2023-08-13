import numpy as np
from sklearn.cluster import KMeans
customer_data = np.array([
    [2.5, 3.5, 4.0, 1.0],
    [1.5, 2.5, 3.5, 0.5],
    [3.0, 4.0, 2.5, 0.8],  
])
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)
kmeans.fit(customer_data)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
new_customer_features = [3.0, 4.0, 2.5, 0.8]
new_customer_cluster = kmeans.predict([new_customer_features])
assigned_cluster_center = cluster_centers[new_customer_cluster][0]
print(f"The new customer belongs to cluster {new_customer_cluster[0]}")
print(f"The cluster center for this segment is: {assigned_cluster_center}")
