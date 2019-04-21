
def subsequences(inp, out, i, j):
    # base case
    if i==len(inp):
        print(''.join(out),end=',')
        return

    # rec case
    # include current char
    out[j] = inp[i]
    subsequences(inp, out, i+1, j+1)

    # exclude current char
    out[j]=''
    subsequences(inp, out, i+1, j)

if __name__=='__main__':
    inp = input()
    out = ['']*(len(inp))

    subsequences(inp, out, 0, 0)
