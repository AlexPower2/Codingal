def pushZerosToEnd(a,size):
    zero=0

    nonzero=0

    while(nonzero!=size):
        if a[nonzero]!=0:
            a[nonzero],a[zero]= a[zero],a[nonzero]
            zero+=1
        nonzero+=1

a=[1,0,5,6,0,0,0,1,2,6,7,45,765]
size=len(a)
print(a)
pushZerosToEnd(a,size)
print("Array after pushing all zeros to end of array: ")
print(a)