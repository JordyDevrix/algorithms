from algorithms import SortAlgs, SearchAlgs

my_list = [5, 6, 42, 86, 98, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7]
my_target = 7


# magic happens inside algorithms.py
print(f"target: {my_target}")
print(my_list)
my_list = SortAlgs.bubble_sort(my_list)
print(my_list)
index = SearchAlgs.binary_search(my_target, my_list)
print(index)


