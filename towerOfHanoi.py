
def towerOfHanoi(n, src, dest, helper):
    # base case
    if n==0:
        return

    # rec case
    # step 1  move n-1 disks from a to b
    
    towerOfHanoi(n-1, src, helper, dest)

    # step 2  move nth disk from a to c

    print('Move disk', n, 'from', src, 'to', dest)

    # step 3   move n-1 disks from b to c

    towerOfHanoi(n-1, helper, dest, src)

if __name__=='__main__':
    n = int(input())
    towerOfHanoi(n, 'A', 'C', 'B')
