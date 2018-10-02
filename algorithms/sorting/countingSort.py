class CountingSortClass:
    name = "Counting sort"
    @staticmethod
    def CountingSort(itemsetCom):
        itemset = list(itemsetCom)
        extreme = CountingSortClass.findMaxAndMin(itemset)
        mini = extreme[0]
        size = extreme[1] - mini  + 1
        del extreme
        count = [0]*size
        for item in itemset:
            count[item-mini] +=1
        for index in range(size-1):
            count[index+1] += count[index]
        output = [0] * count[len(count)-1]
        for item in itemset:
            output[count[item-mini]-1] = item
            count[item-mini] -= 1
        return output

    @staticmethod
    def findMaxAndMin(itemset):
        mini = float('inf')
        maxi = -float('inf')
        for item in itemset:
            if item > maxi:
                maxi = item
            if item < mini:
                mini = item
        return (mini, maxi)