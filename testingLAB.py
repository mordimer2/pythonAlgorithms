from importRef import *
import random

test = TestSortMethods() 
allAlgorithms = [BubbleSortClass.BubbleSort,StupidSortClass.StupidSort, CocktailShakerSortClass.CocktailShakerSort,GnomeSortClass.GnomeSort,SelectionSortClass.SelectionSort,InsertionSortClass.InsertionSort,TreeSortClass.TreeSort,QuicksortClass.Quicksort,PigeonholeSortClass.PigeonholeSort, CountingSortClass.CountingSort,HeapsortClass.Heapsort, MergeSortClass.MergeSort]

#test.TestSortAlgorithm(BubbleSortClass.BubbleSort, BubbleSortClass.name,True, False)
#test.TestSortAlgorithm(CocktailShakerSortClass.CocktailShakerSort, CocktailShakerSortClass.name,True, False)
#test.TestSortAlgorithm(GnomeSortClass.GnomeSort, GnomeSortClass.name,True, False)
#test.TestSortAlgorithm(SelectionSortClass.SelectionSort, SelectionSortClass.name,True, False)
 
#test.TestSortAlgorithm(QuicksortClass.Quicksort, QuicksortClass.name, True, True)
#test.TestSortAlgorithm(TreeSortClass.TreeSort, TreeSortClass.name, False, True)
#test.TestSortAlgorithm(PigeonholeSortClass.PigeonholeSort, PigeonholeSortClass.name,True, True)
#test.TestSortAlgorithm(CountingSortClass.CountingSort, CountingSortClass.name,True, True)
#test.TestSortAlgorithm(HeapsortClass.Heapsort, HeapsortClass.name, True, False)
test.TestSortAlgorithm(MergeSortClass.MergeSort, MergeSortClass.name, True, True)
