iris = {}


def add_iris(id_n, species, petal_length, petal_width, **features):
    details = dict()
    details['species'] = species
    details['petal_length'] = petal_length
    details['petal_width'] = petal_width
    for key, value in features.items():
        details[key] = value
    iris[id_n] = details


# print(iris)
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
# print(iris)
