
keypad = ['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

def printKeypadString(inp, out, i, j):
    # base case
    if i==len(inp):
        print(''.join(out), end=',')
        return

    # rec case
    digit = int(inp[i])

    if (digit == 1 or digit == 0):
        printKeypadString(inp, out, i+1, j)

    for k in range(len(keypad[digit])):
        out[j] = keypad[digit][k]
        printKeypadString(inp, out, i+1, j+1)


if __name__=='__main__':
    inp = input()
    out = [''] * 4

    printKeypadString(inp, out, 0, 0)
