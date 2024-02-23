
class SortAlgs:

    @staticmethod
    def builtin_sort(array: list) -> list:
        array.sort()
        return array

    @staticmethod
    def bubble_sort(array: list) -> list:
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
                return SortAlgs.bubble_sort(array)

        # returning sorted array if counter didn't exceed past 0
        return array

    @staticmethod
    def quick_sort(array: list) -> list:
        for i in range(200):
            pivot = array[-1]
            left_cursor = -1
            for index in range(len(array) - 1):
                right_cursor = index
                if array[right_cursor] < pivot:
                    if array[right_cursor] < array[left_cursor] and left_cursor != -1:
                        # swapping array's element places at the specific indexes
                        (array[right_cursor], array[left_cursor]) = (array[left_cursor], array[right_cursor])
                    left_cursor += 1

            pivot_value = array[-1]
            array[-1] = array[left_cursor]
            array[left_cursor] = pivot_value

            if left_cursor == -1:
                array = array[-1:] + array[:-1]

            counter = 0
            for value in range(len(array) - 1):
                compare = value + 1
                if array[value] <= array[compare]:
                    pass
                elif array[value] > array[compare]:
                    counter += 1

            if counter == 0:
                return array

        return SortAlgs.quick_sort(array)

    @staticmethod
    def __partition(array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1

    # function to perform quicksort

    @staticmethod
    def quick_sort_two(array, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = SortAlgs.__partition(array, low, high)

            # Recursive call on the left of pivot
            SortAlgs.quick_sort_two(array, low, pi - 1)

            # Recursive call on the right of pivot
            SortAlgs.quick_sort_two(array, pi + 1, high)
        return array


class SearchAlgs:

    @staticmethod
    def __binary_search(target, array, right, left: int = 0) -> int or str:
        # if the left pointer exceeds the right pointer, then the item is not inside the list
        if left > right:
            return "not found"

        center = int((left + right) / 2)

        # check if my target is higher than, lower than or equals my center
        if target == array[center]:
            return center
        elif target > array[center]:
            return SearchAlgs.__binary_search(target, array, right, center + 1)
        elif target < array[center]:
            return SearchAlgs.__binary_search(target, array, center - 1, left)

    # 'constructor' for the search engine

    @staticmethod
    def binary_search(target, array: list):
        left = 0
        right = len(array) - 1
        return SearchAlgs.__binary_search(target, array, right, left)
