from algorithms import SortAlgs, SearchAlgs
import time

my_list = [5, 6, 42, 86, 98, 6, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7]
# my_list = [1, 2, 3, 3, 3, 3, 4, 5, 5, 8, 8, 9, 10000]
my_target = 7

start = time.perf_counter() * 1000
print(SortAlgs.quick_sort(my_list))
end = time.perf_counter() * 1000
print(f"{SortAlgs.quick_sort.__name__} speed = {end - start} (multiplied bij 1000)\n")

start = time.perf_counter() * 1000
print(SortAlgs.bubble_sort(my_list))
end = time.perf_counter() * 1000
print(f"{SortAlgs.bubble_sort.__name__} speed = {end - start} (multiplied bij 1000)\n")

start = time.perf_counter() * 1000
print(SortAlgs.builtin_sort(my_list))
end = time.perf_counter() * 1000
print(f"{SortAlgs.builtin_sort.__name__} speed = {end - start} (multiplied bij 1000)\n")
