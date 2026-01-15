class MergeUnsortedUnique:
    def __init__(self, *arrays):
        self.arrays = arrays

    def array_to_tuple(self):
        tuples = [tuple(arr) for arr in self.arrays]
        return tuples

    def tuple_to_merge(self):
        merged = []
        for tup in self.array_to_tuple():
            merged.extend(tup)
        unique = set(merged)
        return list(unique)

    def merge_to_sort(self):
        liste = self.tuple_to_merge()
        n = len(liste)
        for i in range(n):
            for j in range(0, n-i-1):
                if liste[j] > liste[j+1]:
                    liste[j], liste[j+1] = liste[j+1], liste[j]
        return tuple(liste)
    
    def yazdir(self):
        print(list(self.merge_to_sort()))

arr1 = [5, 1, 3]
arr2 = [3, 2, 6]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [4, 2, 2, 4, 4, 2]
arr2 = [2, 2, 1, 4, 5]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [0, -1, 3]
arr2 = [-1, 2, 0]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = []
arr2 = [2, 1]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [5, 3, 8, 1, 9, 1, 2]
arr2 = [2, 8, 7, 1, 6]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [-3, 0, 2, 5, 7, 4]
arr2 = [4, -1, 0, 2, 6]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [10, 3, 8, 1, 6]
arr2 = [5, 7, 2, 9, 4]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [1, 2, 2, 3, 5]
arr2 = [3, 4, 4, 5, 6]
output = MergeUnsortedUnique(arr1, arr2)
output.yazdir()

arr1 = [5, 1, 3]
arr2 = [3, 2, 6]
arr3 = [0, 7, 2]
output = MergeUnsortedUnique(arr1, arr2, arr3)
output.yazdir()

arr1 = [-3, 0, 2]
arr2 = [4, -1, 0]
arr3 = [3, 2, 1]
output = MergeUnsortedUnique(arr1, arr2, arr3)
output.yazdir()

arr1 = [10, 3, 8]
arr2 = [5, 7, 2]
arr3 = [1, 6, 9]
output = MergeUnsortedUnique(arr1, arr2, arr3)
output.yazdir()

arr1 = [1, 2, 2]
arr2 = [3, 2, 4]
arr3 = [4, 5, 1]
output = MergeUnsortedUnique(arr1, arr2, arr3)
output.yazdir()