class StupidSortClass:
    name = "Stupid sort"

    @staticmethod
    def StupidSort(itemsetCom):
        itemset = list(itemsetCom)
        orderChanged = False

        index = 0
        while index < len(itemset):
            currentItem = itemset[index]
            for i in range(index+1, len(itemset)):
                if itemset[i] < currentItem:
                    StupidSortClass.replaceElements(itemset, i, index)
                    orderChanged = True
                    break
            if orderChanged:
                orderChanged = not orderChanged
                continue
            index += 1

        return itemset

    @staticmethod
    def replaceElements(itemset, a, b):
        tmp = itemset[a]
        itemset[a] = itemset[b]
        itemset[b] = tmp