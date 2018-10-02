import time
from smallListsContainer import SmallListsContainer
from largeListsContainer import LargeListsContainer
class TestSortMethods:
    ### method = method used to sort out array
    ### methodName = method name
    ### stable = in case of unstable method, constant, ascending and descending lists are omitted
    ### fast = indicate if algorithm is fast enough to handle more than 10k elemnts in list in limited amount of time
    def TestSortAlgorithm(self, method, methodName, stable, fast):
        print("Sorting method used: " + methodName)
        slc = SmallListsContainer()
        llc = LargeListsContainer()
        if stable:
            for lis in slc.GetNonRecursionLists():
                self.checkSpecyficList(method, lis[2], lis[0], lis[1])

        for lis in slc.GetCommonRandomLists():
            self.checkSpecyficList(method, lis[2], lis[0], lis[1])

        if fast:
            for lis in llc.GetLargeLists(0):
                self.checkSpecyficList(method, lis[2], lis[0], lis[1])
    # END TestAllFromSingleMethod

    def checkSpecyficList(self, sortingMethod, testName, itemset, correctOrder):
        start = time.time()
        output = sortingMethod(itemset)
        result = self.areEqual(correctOrder, output)
        self.interpreteResult(result, testName)
        stop = time.time()
        print("Time: " + str((stop-start)))
    # END check specyfic list
    
    def areEqual(self, correct, result):
        index = 0
        while index < len(correct):
            if correct[index] != result[index]:
                return False
            index+=1
        return True
    # END areEqual

    def interpreteResult(self, result, testNum):
        if result:
            print("Test \"{0}\" accomplished successfully.".format(testNum))
        else:
            print("Test \"{0}\" failed.".format(testNum))
    # END interpreteResult