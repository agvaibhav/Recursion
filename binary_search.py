
def binary_search(a, key, start, end):
    try:
        middle = (start + end)//2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            return binary_search(a, key, start, middle-1)
        else:
            return binary_search(a, key, middle+1, end)
    except:
        return('the no is not present in the array')

if __name__=='__main__':
    a = sorted(list(map(int, input().split())))
    print('sorted array is:', a)
    key = int(input('write the no you want to search:'))
    print('the no is found at index:', binary_search(a, key, 0, len(a)-1))
    
