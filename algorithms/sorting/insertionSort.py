class InsertionSortClass:
    name = "Insertion sort"

    @staticmethod
    def InsertionSort(itemsetCom):
        itemset = list(itemsetCom)
        index = 1

        while index < len(itemset):
            i = index-1
            key = itemset[index]
            while i >= 0 and itemset[i] > key:
                itemset[i+1] = itemset[i]
                i -=1
            itemset[i+1] = key
            index += 1
        # END while

        return itemset
