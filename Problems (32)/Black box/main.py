# use the function blackbox(lst) that is already define
test_list = [1, 2, 3]
test_id = id(test_list)

if test_id == id(blackbox(test_list)):
    print("modifies")
else:
    print("new")