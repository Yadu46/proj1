print("hi, bengaluru")

def hcf(a,b):
    """ This is an hcf calculator using recursive function"""
    if b==0:
        return a
    else:
        return hcf(b, a%b)

print(hcf.__doc__)
