from algorithms import SortAlgs, SearchAlgs
import time
import random

new_list = [5, 6, 42, 86, 98, 6, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7, 5, 6, 2, 20, 340, 328, 32, 44, 566, 63, 4]
"""new_list = [247, 377, 237, 240, 894, 914, 706, 292, 678, 798, 213, 930, 251, 290, 914, 362, 434, 659, 728, 408,
            5, 6, 42, 86, 98, 6, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7, 5, 6, 2, 20, 340, 328, 32, 44, 566, 63, 4,
            31, 91, 52, 18, 92, 17, 70, 97, 17, 56, 53, 65, 1, 4342, 134, 435, 5647, 75, 34, 12, 635, 2, 52, 31, 578,
            21, 32, 33, 4, 38, 421, 44, 52, 522, 53, 56, 158, 61, 623, 65, 65, 70, 75, 80, 84, 86, 91, 92, 397, 98, 134,
            5, 6, 42, 86, 98, 6, 65, 450, 33, 12, 61, 80, 38, 58, 28, 1, 7, 5, 6, 2, 20, 340, 328, 32, 44, 566, 63, 4,
            514, 967, 397, 216, 632, 955, 230, 271, 797, 251, 963, 16, 183, 771, 246, 84]
"""
my_list = [1, 2, 3, 3, 3, 3, 4, 5, 5, 8, 8, 9, 10000]
my_target = 7

size = len(new_list)

start = time.perf_counter() * 1000
print(SortAlgs.quick_sort(new_list))
end = time.perf_counter() * 1000
print(f"{SortAlgs.quick_sort.__name__} speed = {end - start} (multiplied bij 1000)\n")

start = time.perf_counter() * 1000
print(SortAlgs.quick_sort_two(new_list, 0, size - 1))
end = time.perf_counter() * 1000
print(f"{SortAlgs.quick_sort_two.__name__} speed = {end - start} (multiplied bij 1000)\n")

start = time.perf_counter() * 1000
print(SortAlgs.builtin_sort(new_list))
end = time.perf_counter() * 1000
print(f"{SortAlgs.builtin_sort.__name__} speed = {end - start} (multiplied bij 1000)\n")


start = time.perf_counter() * 1000
print(SortAlgs.bubble_sort(new_list))
end = time.perf_counter() * 1000
print(f"{SortAlgs.bubble_sort.__name__} speed = {end - start} (multiplied bij 1000)\n")



