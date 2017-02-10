class Sorter(object):
    """
    Base class for sorters. Defines the `sort` method.
    """
    def sort(self, elements):
        """
        Sorts the elements in the list.

        :param elements: The list of elements which has to be sorted
        :type elements: list
        :return: The sorted list of elements
        :rtype: list
        """
        raise NotImplementedError()


class InsertionSorter(Sorter):
    """
    Sorter implementation using the insertion sort strategy.
    """
    def sort(self, elements: list):
        for i in range(1, len(elements), 1):
            if elements[i] < elements[i - 1]:
                temp = elements[i]
                del elements[i]
                for j in range(0, len(elements), 1):
                    if temp < elements[j]:
                        elements.insert(j, temp)
                        break
        return elements


class QuickSorter(Sorter):
    """
    Sorter implementation using the quick sort strategy.
    """
    def sort(self, elements):
        pivot = len(elements) // 2
        smaller = []
        larger = []
        equal = []
        if len(elements) > 1:
            for i in range(0, len(elements), 1):
                if elements[i] < elements[pivot]:
                   smaller.append(elements[i])
                elif elements[i] == elements[pivot]:
                    equal.append(elements[i])
                else:
                    larger.append(elements[i])
            elements = self.sort(smaller) + equal + self.sort(larger)

        return elements
