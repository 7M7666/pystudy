import random
import time

SIZE = 100000

# 打印数组的函数
def print_array(arr):
    # 由于数组大小为100000，这里只打印前10个元素作为示例
    print(arr[:10], "...")

# 生成随机数的函数
def generate_random_numbers(arr):
    for i in range(SIZE):
        arr.append(random.randint(0, 999))  # 生成0到999之间的随机数

# 冒泡排序的函数
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 快速排序的函数
def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        partition_index = i + 1
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)

# 主函数
if __name__ == "__main__":
    arr = []
    arr_bubble = []
    arr_quick = []

    # 生成随机数
    generate_random_numbers(arr)

    # 打印原始数组
    print("Original array:")
    print_array(arr)

    # 复制数组以进行排序
    arr_bubble = arr.copy()
    arr_quick = arr.copy()

    # 冒泡排序
    start_time = time.time()
    bubble_sort(arr_bubble)
    end_time = time.time()
    print("Bubble Sorted array:")
    print_array(arr_bubble)
    print(f"Bubble Sort time: {end_time - start_time} seconds")

    # 快速排序
    start_time = time.time()
    quick_sort(arr_quick, 0, len(arr_quick) - 1)
    end_time = time.time()
    print("Quick Sorted array:")
    print_array(arr_quick)
    print(f"Quick Sort time: {end_time - start_time} seconds")
