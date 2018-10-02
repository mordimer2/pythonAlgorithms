class SelectionSortClass:
    name = "Selection sort"

    @staticmethod
    def SelectionSort(itemsetCom):
        itemset = list(itemsetCom)
        index = 0

        while index < len(itemset):
            min = itemset[index]
            searchedIndex = index
            for i in range(index, len(itemset)):
                if min > itemset[i]:
                    min = itemset[i]
                    searchedIndex = i
            tmp = itemset[index]
            itemset[index] = itemset[searchedIndex]
            itemset[searchedIndex] = tmp
            index+=1
        # END while

        return itemset