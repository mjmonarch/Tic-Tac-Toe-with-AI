# use the function blackbox(lst) that is already defined
initial_list = [1, 2, 3]
updated_list = blackbox(initial_list)
if id(initial_list) == id(updated_list):
    print("modifies")
else:
    print("new")