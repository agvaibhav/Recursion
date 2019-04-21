
def bubble_sort(a, n):
    if n == 1:
        return

    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

    bubble_sort(a, n-1)

    return a

def rec_bubble_sort(a, j, n):
    if n==1:
        return

    if j == n-1:
        return rec_bubble_sort(a, 0, n-1)

    if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]

    rec_bubble_sort(a, j+1, n)

    return a

if __name__=='__main__':
    a = [2,5,4,8,9,7]
    print(bubble_sort(a, len(a)))
    print(rec_bubble_sort(a, 0, len(a)))
