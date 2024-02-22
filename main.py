my_list = [5, 6, 2, 8, 98, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7]
my_target = 33


def bubble_sort_me(array: list) -> list:
    counter = 0
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            counter += 1
            var_large = array[index]
            var_small = array[index + 1]
            array[index + 1] = var_large
            array[index] = var_small

        if counter > 0:
            return bubble_sort_me(array)

    return array


def _search_me_engine(target, right, left: int = 0) -> int or str:
    if left > right:
        return "not found"

    center = int((left + right) / 2)

    if target == my_list[center]:
        return center
    elif target > my_list[center]:
        return _search_me_engine(target, right, center + 1)
    elif target < my_list[center]:
        return _search_me_engine(target, center - 1, left)


def search_me(target, array: list):
    left = 0
    right = len(array) - 1
    return _search_me_engine(target, right, left)


# print my_list before sorting
print(my_list)

# sorting my_list
my_list = bubble_sort_me(my_list)

# print my_list after sorting
print(my_list)

# binary search on my_list
my_item_index = search_me(target=my_target, array=my_list)

print(f"item index {my_item_index}")
