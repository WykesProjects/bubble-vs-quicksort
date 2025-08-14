import time
import random
import matplotlib.pyplot as plt

# sort algorithms

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# test performance

def test_performance(sizes):
    bubble_times = []
    quick_times = []

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        start = time.time()
        bubble_sort(data)
        end = time.time()
        bubble_times.append(end - start)

        start = time.time()
        quicksort(data)
        end = time.time()
        quick_times.append(end - start)

        print(f"size {size} -> bubble: {bubble_times[-1]:.4f}s, quick: {quick_times[-1]:.4f}s")

    return bubble_times, quick_times

# plot results

def plot_results(sizes, bubble_times, quick_times):
    plt.plot(sizes, bubble_times, label="bubble sort")
    plt.plot(sizes, quick_times, label="quicksort")
    plt.xlabel("input size")
    plt.ylabel("execution time (seconds)")
    plt.title("bubble sort vs quicksort performance")
    plt.legend()
    plt.grid(True)
    plt.savefig("graph.png")
    plt.show()

# main

if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 2000]
    bubble, quick = test_performance(input_sizes)
    plot_results(input_sizes, bubble, quick)