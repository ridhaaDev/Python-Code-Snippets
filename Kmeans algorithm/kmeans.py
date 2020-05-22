#K-Means clustering implementation
import math
import numpy as np   
import pandas as pd
from matplotlib import pyplot as plt
import random

# ====
# Define a function that computes the distance between two data points
def distance(point1, point2):
    part1 = (point1[0] - point2[0]) ** 2
    part2 = (point1[1] - point2[1]) ** 2
    return math.sqrt(part1 + part2)

# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
dataset = pd.read_csv("data1953.csv")
x = dataset.iloc[:, 1]
y = dataset.iloc[:, 2]
data = list(zip(x, y))

k = 3
num_iterations = 7

# # ====
# # Write the initialisation procedure
centroids = random.sample(data, k)

for centroid in centroids:
    plt.scatter(centroid[0], centroid[1], c="black")

# ====
# Implement the k-means algorithm, using appropriate looping
for iteration in range(num_iterations):
    classifications = {}

    for i in range(k):
        classifications[i] = []

    # Assign each point to its closest centroid
    for point in data:
        distances = [distance(point, centroid) for centroid in centroids]
        classification = distances.index(min(distances))
        classifications[classification].append(point)

    for index in classifications:
        one_class = classifications[index]
        x_val = [x[0] for x in one_class]
        y_val = [x[1] for x in one_class]
        plt.xlabel("Birth rate")
        plt.ylabel("Life Expectancy")
        plt.scatter(x_val, y_val)

    prev_centroids = centroids

    # Updating the centroids to the average
    for classification in classifications:
        centroids[classification] = np.average(classifications[classification], axis=0)
        current_centroid = centroids[classification]
        plt.scatter(current_centroid[0], current_centroid[1], c="black")
       
    plt.show()

