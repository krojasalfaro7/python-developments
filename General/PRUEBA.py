# x = 10
# x2 = 1
# while x > 7:
#     x = x -1
#     while x2 < 10:
#         x2 += 1
#         x += x2 -1
# if x > x2:
#     print(x2-x)
# else:
#     print(x+x2)

# a = True
# b = False
# c = False
#
# if not a or b and c:
#     print(1)
# elif not a or not b and c and a:
#     print(2)
# elif not a and b and not b and a or c:
#     print(3)
# else:
#     print(4)


# x = 100
# y = 101
# z = 102
#
# while x < y and z > y and x+2 >=z:
#     x = y -3
#     z = z -2
#     y = x -1
# print(x,y,z)

# print([i+j for i in "abc" for j in "def"])

# i=0
# def change(i):
#     i=i+1
#     return i
# change(1)
# print(i)


# a = [1,2,3,4,5]
# for i in range(1, 5):
#     a[i-1] = a[i]
# for i in range(0, 5):
#     print(a[i])

# a = {'B':5, 'A':9, 'C':7}
# algo = sorted(a)
# print(algo)

# dta = ({'seq': 10, 'id': 18}, {'seq': 20, 'id': 42}, {'seq': 30, 'id': 20})
# x = 0
# for dt in dta:
#     x += dt.get('seq')%5
#     if dt.get('id')/10==dt.get('seq')/5:
#         x=dt.get('seq')
# print(x)


# n = 2;
# st = "P"
# for i in range(n):
#     for j in range(i):
#         st += 'A'
#     st+="B"
# for i in range(n, 0, -1):
#     for j in range(i):
#         st+="C"
#     st+="D"
# print(st)

