


def to_dict(*lst):
    dict = {}
    for item in lst:
        dict[item] = item
    return dict


print(to_dict(1, 2, 3, 4))
