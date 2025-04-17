import time
import sys
# import statistics
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

inputList.append('10mills_datasets_gitignored/half_sorted_5m.txt')
inputList.append('10mills_datasets_gitignored/random_numbers_5m.txt')
inputList.append('10mills_datasets_gitignored/reverse_5m-float.txt')
inputList.append('10mills_datasets_gitignored/Sorted_5m.txt')

inputList.append('10mills_datasets_gitignored/half_sorted_10m.txt')
inputList.append('10mills_datasets_gitignored/random_numbers_10m.txt')
inputList.append('10mills_datasets_gitignored/reverse_10m-float.txt')
inputList.append('10mills_datasets_gitignored/Sorted_10m.txt')


# sortingAlgos=[TimSort, introsort, heap_sort, quickSort, mergeSort,
#               selectionSort, insertion_sort ,bubble_sort]

sortingAlgos=[Hybrid_sort_700_run, TimSort, introsort, mergeSort, bubble_sort]


sys.setrecursionlimit(1000000000) # python's default recusion limit is 1000. Need this for quick sort sorted input case

for algo in sortingAlgos:
        
    print("--------------------------------------------")
    print(f"{algo.__name__} times: ")
    
    for path in inputList:
        
        print(f"path: {path.split('/')[1]}")
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
                start = time.perf_counter()
                quickSort(inputarray, 0, len(inputarray) - 1)
                end = time.perf_counter()
            elif(algo is heap_sort):
                start = time.perf_counter()
                heap_sort(inputarray)
                end = time.perf_counter()
            elif(algo is introsort):
                start = time.perf_counter()
                introsort(inputarray)
                end = time.perf_counter()
            elif(algo is bubble_sort):
                start = time.perf_counter()
                bubble_sort(inputarray)
                end = time.perf_counter()
            elif(algo is TimSort):
                start = time.perf_counter()
                TimSort(inputarray)
                end = time.perf_counter()
            elif(algo is selectionSort):
                start = time.perf_counter()
                selectionSort(inputarray, len(inputarray))
                end = time.perf_counter()
            elif(algo is insertion_sort):
                start = time.perf_counter()
                insertion_sort(inputarray)
                end = time.perf_counter()
            elif(algo is mergeSort):
                start = time.perf_counter()
                mergeSort(inputarray, 0, len(inputarray)-1)
                end = time.perf_counter()
            elif(algo is Hybrid_sort_700_run):
                start = time.perf_counter()
                Hybrid_sort_700_run(inputarray)
                end = time.perf_counter()
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

            
