
class SortingAlgs:

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
                return SortingAlgs.bubble_sort(array)

        # returning sorted array if counter didn't exceed past 0
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
