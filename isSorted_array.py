# to check if the given array is sorted

def isSorted(a, n):
    if n == 1:
        return True

    if(a[0]<a[1] and isSorted(a[1:], n-1)):
       return True
    else:
        return False

if __name__ == '__main__':
    a = [1,2,31,5,8]
    n = len(a)
    print(isSorted(a, n))
