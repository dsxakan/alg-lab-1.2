import time

def shell_sort(arr):
    """
    Сортировка Шелла
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def heap_sort(arr):
    """
    Пирамидальная сортировка
    """
    n = len(arr)

    # Строим пирамиду
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Сортируем пирамиду
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    """
    Восстанавливаем пирамиду
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def quick_sort(arr):
    """
    Сортировка Хоара
    """
    n = len(arr)

    if n <= 1:
        return

    pivot = arr[n // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    quick_sort(left)
    quick_sort(right)

    arr[:len(left)] = left
    arr[len(left):len(left) + len(middle)] = middle
    arr[len(left) + len(middle):] = right

# Сортировка массива
arr = [10, 7, 8, 9, 1, 5]

# Сортировка Шелла
shell_sort(arr)
print("После сортировки Шелла:", arr)

# Пирамидальная сортировка
arr = [10, 7, 8, 9, 1, 5]
heap_sort(arr)
print("После пирамидальной сортировки:", arr)

# Сортировка Хоара
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print("После сортировки Хоара:", arr)
