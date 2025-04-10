import time
import sys
from bubble import bubble_sort
from introSort import introsort
from heapSort import heap_sort
from quickSort import quickSort
from timSort import TimSort
from selectionSort import selectionSort
from insertionSort import insertion_sort
from mergeSort import mergeSort

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

inputList.append('Reversed/reverse_1000-float.txt')
inputList.append('Reversed/reverse_5000-float.txt')
inputList.append('Reversed/reverse_10000-float.txt')
inputList.append('Reversed/reverse_50000-float.txt')
inputList.append('Reversed/reverse_100000-float.txt')
    
inputList.append('Sorted/Sorted_1000.txt')
inputList.append('Sorted/Sorted_5000.txt')
inputList.append('Sorted/Sorted_10000.txt')
inputList.append('Sorted/Sorted_50000.txt')
inputList.append('Sorted/Sorted_100000.txt')


# ------------------------------------------------

# inputList.append('Sorted/Sorted_50000.txt')

# inputList.append('Random/random_numbers_1000.txt')
# inputList.append('Reversed/reverse_1000-float.txt')
# inputList.append('Sorted/Sorted_1000.txt')

sortingAlgos=[TimSort, quickSort, heap_sort, introsort, 
              selectionSort, insertion_sort ,bubble_sort]

sys.setrecursionlimit(1000000) # python's default recusion limit is 1000. Need this for quick sort sorted input case

for algo in sortingAlgos:
    
    print("--------------------------------------------")
    print(f"{algo.__name__} times: ")
    
    for path in inputList:
        
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
        else:
            print(f"{algo} is not defined properly")  
                  
        print(f"Time taken for {path.split("/")[1]}: {end-start:.4f}")
