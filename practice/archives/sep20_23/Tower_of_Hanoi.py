n = int(input())
print((1<<n)-1)

def hanoi(start,end,mid,size):
    if size == 1:
        print(start,end)
        return
    hanoi(start,mid,end,size-1)
    print(start,end)
    hanoi(mid,end,start,size-1)
hanoi(1,3,2,n)