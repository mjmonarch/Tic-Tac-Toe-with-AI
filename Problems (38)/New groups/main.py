# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
number_of_groups = int(input())
groups_2021 = {groups[item]: int(input()) for item in range(number_of_groups)}
groups_2021.update({groups[item]: None for item in range(number_of_groups, 9)})

print(groups_2021)
