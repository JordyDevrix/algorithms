
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
                        right_value = array[right_cursor]
                        left_value = array[left_cursor]
                        array[right_cursor] = left_value
                        array[left_cursor] = right_value
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
