import time
import sys
import statistics
import numpy as np
from bubble import bubble_sort
from introSort import introsort
from heapSort import heap_sort
from quickSort import quickSort
from timSort import TimSort
from selectionSort import selectionSort
from insertionSort import insertion_sort
from mergeSort import mergeSort
from basis import Hybrid_sort_700_run

inputList = ['Half_Sorted/half_sorted_1000.txt']    

inputList.append('Half_Sorted/half_sorted_5000.txt')
inputList.append('Half_Sorted/half_sorted_10000.txt')
inputList.append('Half_Sorted/half_sorted_50000.txt')
inputList.append('Half_Sorted/half_sorted_100000.txt')
    
inputList.append('Random/random_numbers_1000.txt')
inputList.append('Random/random_numbers_5000.txt')
inputList.append('Random/random_numbers_10000.txt') 
inputList.append('Random/random_numbers_50000.txt') 
inputList.append('Random/random_numbers_100000.txt')
#100m

inputList.append('Reversed/reverse_1000-float.txt')
inputList.append('Reversed/reverse_5000-float.txt')
inputList.append('Reversed/reverse_10000-float.txt')
inputList.append('Reversed/reverse_50000-float.txt')
inputList.append('Reversed/reverse_100000-float.txt')
#100m
    
inputList.append('Sorted/Sorted_1000.txt')
inputList.append('Sorted/Sorted_5000.txt')
inputList.append('Sorted/Sorted_10000.txt')
inputList.append('Sorted/Sorted_50000.txt')
inputList.append('Sorted/Sorted_100000.txt')
#50m
#100m

inputList.append('largeDatasets/half_sorted_50m.txt')
inputList.append('largeDatasets/half_sorted_100m.txt')
inputList.append('largeDatasets/random_numbers_50m.txt')
inputList.append('largeDatasets/reverse_50m-floats.txt')

## try for 100m random, reverse later


# inputList = ['largeDatasets/half_sorted_50m.txt']
# inputList.append('largeDatasets/half_sorted_100m.txt')
# inputList.append('largeDatasets/random_numbers_50m.txt')
# inputList.append('largeDatasets/reverse_50m-floats.txt')
# inputList.append('largeDatasets/Sorted_50m.txt')
# inputList.append('largeDatasets/Sorted_100m.txt')
 
# ------------------------------------------------
# inputList.append('Sorted/Sorted_50000.txt')

# inputList.append('Random/random_numbers_1000.txt')
# inputList.append('Reversed/reverse_1000-float.txt')
# inputList.append('Sorted/Sorted_1000.txt')

# sortingAlgos=[TimSort, introsort, heap_sort, quickSort, mergeSort,
#               selectionSort, insertion_sort ,bubble_sort]

# sortingAlgos=[Hybrid_sort_700_run]

# sortingAlgos=[TimSort]
# sortingAlgos=[introsort]
# sortingAlgos = [mergeSort]
sortingAlgos = [bubble_sort]


# sortingAlgos=[heap_sort, quickSort]


# sortingAlgos = [selectionSort]

# sortingAlgos = [insertion_sort]



sys.setrecursionlimit(1000000000) # python's default recusion limit is 1000. Need this for quick sort sorted input case

for algo in sortingAlgos:
        
    print("--------------------------------------------")
    print(f"{algo.__name__} times: ")
    
    for path in inputList:
        
        print(f"path: {path.split("/")[1]}")
        iterationTimes=[]
            
        for i in range(1, 100):
            
            with open(path,'r') as fin:
                lines = fin.readlines()
            
            inputarray = [line for line in lines]
            
            '''if("float" in path or "Sorted/Sorted" in path):
                inputarray = [float(line) for line in lines]        
            else:
                inputarray = [int(line) for line in lines]
            '''        
            # print(inputarray[1:10])
            
            if(algo is quickSort):
                start = time.time()
                quickSort(inputarray, 0, len(inputarray) - 1)
                end = time.time()
            elif(algo is heap_sort):
                start = time.time()
                heap_sort(inputarray)
                end = time.time()
            elif(algo is introsort):
                start = time.time()
                introsort(inputarray)
                end = time.time()
            elif(algo is bubble_sort):
                start = time.time()
                bubble_sort(inputarray)
                end = time.time()
            elif(algo is TimSort):
                start = time.time()
                TimSort(inputarray)
                end = time.time()
            elif(algo is selectionSort):
                start = time.time()
                selectionSort(inputarray, len(inputarray))
                end = time.time()
            elif(algo is insertion_sort):
                start = time.time()
                insertion_sort(inputarray)
                end = time.time()
            elif(algo is mergeSort):
                start = time.time()
                mergeSort(inputarray, 0, len(inputarray)-1)
                end = time.time()
            elif(algo is Hybrid_sort_700_run):
                start = time.time()
                Hybrid_sort_700_run(inputarray)
                end = time.time()
            else:
                print(f"{algo} is not defined properly")  
            
            timeTaken = end-start        
            # print(f"Time taken for {path.split("/")[1]}: {timeTaken:.4f}")
            iterationTimes.append(timeTaken)    
            
        _std = np.std(iterationTimes)
        _median = np.median(iterationTimes)
        _mean = np.mean(iterationTimes)
        _max = np.max(iterationTimes)
        _min = np.min(iterationTimes)

        print("""Execution time summary:
        {:^12} {:^12} {:^12} {:^12} {:^12}
        {:^12.4f} {:^12.4f} {:^12.4f} {:^12.4f} {:^12.4f}
                        """.format(
                    "mean (ms)",
                    "median (ms)",
                    "max (ms)",
                    "min (ms)",
                    "std (ms)",
                _mean * 1000,
                _median * 1000,
                _max * 1000,
                _min * 1000,
                _std * 1000,
                    ))

        # print(f"mean: {meanval:.3f}")
        # print(f"median: {medianval:.3f}")
        # print(f"max: {maxval:.3f}")
        # print(f"min: {minval:.3f}")
        # print(f"std: {stdeviation:.3f}")
            
