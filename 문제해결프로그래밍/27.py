from math import sqrt

def population_std(x, y, z):
    values= [x, y, z]
    mean= sum(values) / len(values)
    variance= sum((value- mean) ** 2 for value in values) / len(values)
    return sqrt(variance)

print(round(population_std(3, 5, 7), 4))
print(round(population_std(-3, 0, 3), 4))
