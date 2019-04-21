# we are given a 4xn block and 1x4 and 4x1 tiles
# we have to find out how many ways the block can be filled with the given tiles

def tiles(n):
    if n<=3:
        return 1

    if n==4:
        return 2

    else:
        return(tiles(n-1) + tiles(n-4))



if __name__=='__main__':
    n = int(input('write the no of columns:'))
    print(tiles(n))
