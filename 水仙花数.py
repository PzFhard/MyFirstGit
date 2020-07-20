#水仙花数

import time
#方法一
def one():
    t1 = time.time()
    for i in range(100,1000):

        a=i//100     #取百位
        b = (i-a*100)//10   #取十位
        c = (i - a * 100 - b * 10)   #取个位
        # print(i,a,b,c)
        if i == pow(a,3)+pow(b,3)+pow(c,3):
            print(i)
    t2 = time.time()
    print('one运行时长：',t2-t1)

#方法二
def two():
    t1 = time.time()
    lis=[]
    for i in range(100,1000):
        a = str(i)[0]
        b = str(i)[1]
        c = str(i)[2]
        if i == int(a)**3+int(b)**3+int(c)**3:
            lis.append(i)
    print(lis)
    t2 = time.time()
    print('two运行时长：',t2-t1)
if __name__ == '__main__':
    one()
    # two()



