class QuicksortClass:
    name = "Quicksort"
    @staticmethod
    def Quicksort(itemsetCom):
        itemset = list(itemsetCom)
        QuicksortClass.quicksort(itemset, 0, len(itemset)-1)
        return itemset

    @staticmethod
    def quicksort(itemset, start, end):
        if start < end:
            currentPosition = QuicksortClass.divideAndConquer(itemset, start, end)
            QuicksortClass.quicksort( itemset, start, currentPosition -1)
            QuicksortClass.quicksort( itemset, currentPosition+1, end)
    #END quicksort

    @staticmethod
    def divideAndConquer(itemset, start, end):
        middle = start + int((end-start)/2)
        value = itemset[middle]
        QuicksortClass.replaceElements(itemset, middle, end)
        currentPosition = start
        for i in range(start, end):
            if itemset[i] < value:
                QuicksortClass.replaceElements(itemset, i, currentPosition)
                currentPosition +=1 
        # END for
        QuicksortClass.replaceElements(itemset, currentPosition, end)
        return currentPosition
    #END divideAndConquer
    @staticmethod
    def replaceElements(container, indexA, indexB):
        tmp = container[indexA]
        container[indexA] = container[indexB]
        container[indexB] = tmp
# END quicksort