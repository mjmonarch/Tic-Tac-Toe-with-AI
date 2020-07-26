# the list "walks" is already defined
# your code here

distances = [walk['distance'] for walk in walks]
print(round(sum(distances) / len(distances)))
