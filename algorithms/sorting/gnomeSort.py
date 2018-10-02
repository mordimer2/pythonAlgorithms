class GnomeSortClass:
    name = "Gnome sort"

    @staticmethod
    def GnomeSort(itemsetCom):
        itemset = list(itemsetCom)
        currentIndex = 1
        while currentIndex < len(itemset):
            if itemset[currentIndex- 1] > itemset[currentIndex]:
                tmp = itemset[currentIndex]
                itemset[currentIndex] = itemset[currentIndex -1]
                itemset[currentIndex-1] = tmp
                currentIndex -= 1
                if currentIndex == 0:
                    currentIndex = 1
            else:
                currentIndex += 1
        # END while

        return itemset