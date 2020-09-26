def add_viewer(name, fan_list=None):
    if fan_list is not None:
        fan_list.append(name)
        return fan_list
    else:
        fan_list = [name]
        return fan_list
