def selection_sort(my_list):
    for i in range(0, len(my_list) - 1):
        smallest = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[smallest]:
                smallest = j
        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (j >= 0 and temp < my_list[j]):
            my_list[j + 1] = my_list[j]
            j = j - 1
        my_list[j + 1] = temp

def merge_sort(my_list, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(my_list, start, mid)
        merge_sort(my_list, mid, end)
        merge_list(my_list, start, mid, end)
 
def merge_list(my_list, start, mid, end):
    left = my_list[start:mid]
    right = my_list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            my_list[k] = left[i]
            i = i + 1
        else:
            my_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            my_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            my_list[k] = right[j]
            j = j + 1
            k = k + 1

def quicksort(my_list, start, end):
    if end - start > 1:
        p = partition(my_list, start, end)
        quicksort(my_list, start, p)
        quicksort(my_list, p + 1, end)
 
 
def partition(my_list, start, end):
    pivot = my_list[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and my_list[i] <= pivot):
            i = i + 1
        while (i <= j and my_list[j] >= pivot):
            j = j - 1
 
        if i <= j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
        else:
            my_list[start], my_list[j] = my_list[j], my_list[start]
            return j


while True:
    print("Menu \n1.Selection Sort \n2.Insertion Sort \n3.Merge Sort \n4.Quick Sort")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        my_list = []
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = int(input())
            my_list.append(ele)
        print("Unsorted list",my_list)
        selection_sort(my_list)
        print('Sorted list: ', end='')
        print(my_list)
        break

    elif choice == 2:
        my_list = []
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = int(input())
            my_list.append(ele)
        print("Unsorted list",my_list)
        insertion_sort(my_list)
        print('Sorted list: ', end='')
        print(my_list)
        break

    elif choice == 3:
        my_list = []
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = int(input())
            my_list.append(ele)
        print("Unsorted list",my_list)
        merge_sort(my_list, 0, len(my_list))
        print('Sorted list: ', end='')
        print(my_list)
        break

    elif choice == 4:
        my_list = []
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = int(input())
            my_list.append(ele)
        print("Unsorted list",my_list)
        quicksort(my_list, 0, len(my_list))
        print('Sorted list: ', end='')
        print(my_list)
        break
    
    else:
        print("Invalid choice")
        break