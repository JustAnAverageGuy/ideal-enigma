import sys 
 
input_str = sys.stdin.read() 
input_lines = input_str.split('\n') 
n = int(input_lines[0]) 
cars = [] 
for i in range(1, n+1): 
  cars.append(int(input_lines[i])) 
k = int(input_lines[n+1])
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
 
def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
 
def rooflength(n, cars, k):
    quickSort(cars, 0, n-1)
    temp = []
    for i in range(len(cars)):
        lengths = cars[i + k-1] - cars[i]
        temp.append(lengths)
    return min(temp) + 1

