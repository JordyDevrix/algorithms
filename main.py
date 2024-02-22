my_list = [5, 6, 42, 86, 98, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7]
my_target = 33


def bubble_sort_me(array: list) -> list:
    counter = 0
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            # swapping the array elements from their places. and
            counter += 1
            var_large = array[index]
            var_small = array[index + 1]
            array[index + 1] = var_large
            array[index] = var_small

        # if counter is larger than 0, redo the array until counter is 0
        if counter > 0:
            return bubble_sort_me(array)

    # returning sorted array if counter didn't exceed past 0
    return array


def _search_me_engine(target, right, left: int = 0) -> int or str:
    # if the left pointer exceeds the right pointer, then the item is not inside the list
    if left > right:
        return "not found"

    center = int((left + right) / 2)

    # check if my target is higher than, lower than or equals my center
    if target == my_list[center]:
        return center
    elif target > my_list[center]:
        return _search_me_engine(target, right, center + 1)
    elif target < my_list[center]:
        return _search_me_engine(target, center - 1, left)


# 'constructor' for the search engine
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
