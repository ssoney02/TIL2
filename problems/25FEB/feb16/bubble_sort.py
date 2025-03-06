def bubble_sort(a, n):
    for i in range(n-1, 0, -1):
        print(i)
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(arr)

arr = [55, 7, 78, 12, 41]

bubble_sort(arr, 5)
print(arr)