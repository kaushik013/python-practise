

# ⁡⁣⁣⁢pallindrom or not⁡

def pallind(str):
    rev = ''
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]
    
    if(rev == str):
        print('pallind rom',rev)
    else:
        print('not pallind rom')
# (pallind('ma\'am'))


# ⁡⁣⁣⁢pallindrom⁡ ⁡⁣⁣⁢or not⁡

def pallindrom(st):
    reverse = ''
    for i in range(len(st)-1,-1,-1):
        reverse = reverse + st[i]
    
    if (reverse == st):
        print(f'{reverse} is a pallind rom')
    else:
        print(f'{reverse} is not pallind rom')

pallindrom('saras')
