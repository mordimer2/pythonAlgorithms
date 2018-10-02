### complexity O(n^2)
class BubbleSortClass:
    name = "Bubble sort"

    @staticmethod
    def BubbleSort(itemsetCom):
        itemset = list(itemsetCom)
        anythingChanged = True

        while anythingChanged:
            anythingChanged = False
            index = 0
            while index < len(itemset) - 1:
                if itemset[index] > itemset[index + 1]:
                    tmp = itemset[index + 1]
                    itemset[index + 1] = itemset[index]
                    itemset[index] = tmp
                    anythingChanged = True
                index += 1
            # END while
        #END while
        return itemset