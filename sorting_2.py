import random
def gen():
    b = []
    for i in range(N):
        b.append(random.randint(1, 20))
    return b

def bubble(arr):
    for i in range(N-1):
        for j in range(N - i - 1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b [j+1], b[j]

def sel_sort(arr):
  
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range (i+1, n):
            if arr[j] < arr[m]:
                m = j
            arr[i], arr [m] = arr[m], arr[i]
N = 10
b = gen()
print(b)
sel_sort(b)
print(b)