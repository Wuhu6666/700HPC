import time
from bubble import bubble_sort
from introSort import introsort
from heapSort import heap_sort
from quickSort import quickSort

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

sortingAlgos=[quickSort, heap_sort , introsort, bubble_sort]

for algo in sortingAlgos:
    
    print(f"{algo.__name__} times: ")
    
    for path in inputList:
        
        with open(path,'r') as fin:
            lines = fin.readlines()
            
        if("float" in path or "Sorted/Sorted" in path):
            inputarray = [float(line) for line in lines]        
        else:
            inputarray = [int(line) for line in lines]
        
        # print(inputarray[1:10])
        start = time.time()
        
        if(algo is quickSort):
            # quickSort(inputarray, 0, len(inputarray)-1)
            print("quick sort subdued temporarily")
        elif(algo is heap_sort):
            heap_sort(inputarray)
        elif(algo is introsort):
            introsort(inputarray)
        elif(algo is bubble_sort):
            bubble_sort(inputarray)
        else:
            print(f"{algo} is not defined properly")  
                  
        end = time.time()

        print(f"Time taken for {path.split("/")[1]}: {end-start:.4f}")
