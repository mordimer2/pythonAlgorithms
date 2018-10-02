from math import fabs
from itertools import repeat

class PigeonholeSortClass:
    name = "Pigeonhole sort"
    @staticmethod
    def PigeonholeSort(itemsetCom):
        itemset = list(itemsetCom)
        minMax = PigeonholeSortClass.findMinAndMax(itemset)
        mi = minMax[0]
        size = minMax[1]-mi+1
        del minMax
        holes = [0] * size
        for item in itemset:
            holes[item - mi] +=1
        
        output = []
        for index in range(len(holes)):
            if holes[index] != 0:
                output.extend(repeat(index+mi,holes[index]))
        return output

    @staticmethod
    def findMinAndMax(itemset):
        min = float('inf')
        max = -float('inf')
        for i in range(len(itemset)):
            if min > itemset[i]:
                min = itemset[i]
            if max < itemset[i]:
                max = itemset[i]
        return (int(min), int(max))