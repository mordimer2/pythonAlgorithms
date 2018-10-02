class MergeSortClass:
    name = "Merge sort"

    @staticmethod
    def MergeSort(itemsetCom):
        itemset = list(itemsetCom)
        return MergeSortClass.divideAndConquer(itemset, 0, len(itemset)-1)


    @staticmethod
    def divideAndConquer(tab, start, end):
        if start == end:
            return [tab[start]]
        if start >end:
            return None
        mid = int((start+end)/2)
        tab1= MergeSortClass.divideAndConquer(tab, start, mid)
        tab2 = MergeSortClass.divideAndConquer(tab, mid+1, end)
        if tab1 is None and tab2 is not None:
            return tab2
        elif tab2 is None and tab1 is not None:
            return tab1

        i1=0
        i2=0
        toRet = []
        while True:
            if i1 < len(tab1):
                if i2<len(tab2):
                    if tab1[i1] < tab2[i2]:
                        toRet.append(tab1[i1])
                        i1 +=1
                    else:
                        toRet.append(tab2[i2])
                        i2+=1
                else:
                    for j in range(i1, len(tab1)):
                        toRet.append(tab1[j])
                    break
            else:
                for j in range(i2, len(tab2)):
                    toRet.append(tab2[j])
                break
        return toRet
        #END while
    # END divide and conquer

        