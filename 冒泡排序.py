
#冒泡排序

def paopao(lis):
    n = len(lis)
    for i in range(n):
        for j in range(0,n-i-1):
            if lis[j] < lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    print(lis)


a = [1,3,45,6,7,8]
paopao(a)
