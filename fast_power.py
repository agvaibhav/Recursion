
def power(a, b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

def fast_power(a, b):
    if b==0:
        return 1

    smallAns = fast_power(a, b//2)
    smallAns *= smallAns
    
    if b%2!=0:
        ans = a * smallAns
    elif b%2==0:
        ans = smallAns

    return ans
        

if __name__=='__main__':
    a = int(input("write the no whose power you want to compute:"))
    b = int(input('write the power :'))
    print(power(a,b))
    print(fast_power(a, b))
