
#快速排序
# def binary_chop(alist, data):
#     """
#     非递归解决二分查找
#     """
#     n = len(alist)
#     first = 0
#     last = n - 1
#     while first <= last:
#         mid = (last+first)//2
#         if alist[mid] > data:
#             last = mid - 1
#         elif alist[mid] < data:
#             first = mid + 1
#         else:
#             print(mid)
#             return True
#     return False
#
# lis = []
# for i in range(5,10):
#     lis.append(i)
# print(lis)
# print(len(lis))
# b = binary_chop(lis,1)
# print(b)

