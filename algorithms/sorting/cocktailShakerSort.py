class CocktailShakerSortClass:
    name = "Cocktail shaker sort"

    @staticmethod
    def CocktailShakerSort(itemsetCom):
        itemset = list(itemsetCom)
        anythingChanged = True
        while anythingChanged:
            anythingChanged = False
            index = 0
            while index < len(itemset)-1:
                if itemset[index] > itemset[index+1]:
                    tmp = itemset[index + 1]
                    itemset[index + 1] = itemset[index]
                    itemset[index] = tmp
                    anythingChanged = True
                index += 1

            while index > 0:
                if itemset[index] < itemset[index-1]:
                    tmp = itemset[index - 1]
                    itemset[index - 1] = itemset[index]
                    itemset[index] = tmp
                    anythingChanged = True
                index -= 1
        # END While
        return itemset