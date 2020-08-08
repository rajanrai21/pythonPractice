x=int(input())
try:
    if x>100 or x<0:
        raise ValueError
except:
    print('Input integer value must be between 0 and 100.')

