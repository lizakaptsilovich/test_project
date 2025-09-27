#12.23б - массив из нулей с единицами в определенных позициях
# n=[]
# for i in range(5):
#     n.append([])
#     for j in range(5):
#         n[i].append(0)
# #это мы создали список с пятью подсписками, в каждом 5 нулей
# ch =1
# for i in range(5):
#     for j in range(5):
#         if i==j or i+j==4 or j==2 or i==2:
#             n[i][j]=ch
# for i in range(len(n)):
#     for j in range(len(n)):
#         print(n[i][j], end=' ')
#     print()

#12.24a
# n=[]
# for i in range(5):
#     n.append([])
#     for j in range(5):
#         n[i].append(1)
# for i in range(1):
#     for j in range(1,len(n[0])):
#         n[i][j]=j+1
# for i in range(1,5):
#     for j in range(1,len(n)):
#         n[i][j]=n[i-1][j]+n[i][j-1]
# for i in range(len(n)):
#     for j in range(len(n)):
#         print(n[i][j], end='\t')
#     print()

#12.24b
# n=[]
# for i in range(5):
#     n.append([])
#     for j in range(5):
#         n[i].append(1)
# for i in range(1):
#     for j in range(1,len(n[0])):
#         n[i][j]=j+1
# for i in range(1,5):
#     for j in range(len(n)):
#         n[i][j]=n[i-1][j]+1
#         if n[i-1][j]+1==7:
#             n[i][j]=1
# for i in range(len(n)):
#     for j in range(len(n)):
#         print(n[i][j], end='\t')
#     print()

#12.25
# n=[]
# for i in range(10):
#     n.append([])
#     for j in range(10):
#         n[i].append(1)
# for i in range(1):
#     for j in range(1,10):
#         n[i][j]=n[i][j-1]+1
# for i in range(1,10):
#     for j in range(10):
#         n[i][j]=n[i-1][j]+10
# for i in range(10):
#     for j in range(10):
#         print(n[i][j], end='\t')
#     print()

#12.25b
# n=[]
# for i in range(10):
#     n.append([])
#     for j in range(10):
#         n[i].append(1)
# for i in range(1,10):
#     for j in range(1):
#         n[i][j]=n[i-1][j]+1
# for i in range(10):
#     for j in range(1,10):
#         n[i][j]=n[i][j-1]+10
# for i in range(10):
#     for j in range(10):
#         print(n[i][j], end='\t')
#     print()


#12.25b
# n=[]
# for i in range(10):
#     n.append([])
#     for j in range(10):
#         n[i].append(10)
# for i in range(1):
#     for j in range(1,10):
#         n[i][j]=n[i][j-1]-1
# for i in range(1,10):
#     for j in range(10):
#         n[i][j]=n[i-1][j]+10
# for i in range(10):
#     for j in range(10):
#         print(n[i][j], end='\t')
#     print()


#12.28
# mas = []
# n=5
# k = 0
# for i in range(5): #for 5x5 matrix - make diagonal equal 1
#     mas.append([])
#     for j in range(n):
#         mas[i].append(0)
# m=5
# for f in range(0,3,1):
#     if k < 24:
#         for j in range(f, m-1-f,1):
#                 k+=1
#                 mas[f][j] = k
#         for i in range(0+f, m-1-f, 1):
#                     k+=1
#                     mas[i][m-1-f] = k
#         for j in range(m-1-f,0+f,-1):
#             k +=1
#             mas[m-1-f][j] =k
#         for i in range(m-1-f,0+f,-1):
#             k+=1
#             mas[i][f] = k
#     else:
#         k += 1
#         mas[f][f] = 25
# for i in range(len(mas)):
#     for j in range(len(mas[i])):
#         print(mas[i][j], end = "\t")
#     print()

#спираль
# mas = []
# n = (int(input()))
# for i in range(5): #for 5x5 matrix - make diagonal equal 1
#     mas.append([])
#     for j in range(n):
#         mas[i].append(0)
# a=0
# b=n-1
# c=n-1
# d=0
# ch=1
# while ch<=n*n:
#     for i in range(d,b+1, 1):
#         mas[a][i]=ch
#         ch+=1
#     a+=1
#     for i in range(a, c+1):
#         mas[i][b] = ch
#         ch+=1
#     b-=1
#     for i in range(b,d-1, -1):
#         mas[c][i] = ch
#         ch+=1
#     c -=1
#     for i in range (c, a-1, -1):
#         mas[i][d]=ch
#         ch+=1
#     d+=1
# for i in range(len(mas)):
#     for j in range(len(mas[i])):
#         print(mas[i][j], end = "\t")
#     print()



#12.57
# ss = [
#     [50, 52, 53, 55, 54, 56, 58, 57, 59, 60, 61, 62],
#     [45, 47, 48, 48, 49, 50, 51, 52, 53, 53, 54, 55],
#     [60, 60, 61, 62, 63, 63, 64, 65, 65, 66, 67, 68],
#     [40, 41, 42, 43, 43, 44, 45, 46, 47, 47, 48, 49],
#     [55, 55, 56, 57, 57, 58, 59, 60, 61, 62, 63, 64],
#     [48, 49, 50, 51, 51, 52, 53, 54, 55, 56, 57, 58],
#     [52, 53, 54, 55, 55, 56, 57, 58, 59, 60, 61, 62],
#     [46, 47, 48, 49, 49, 50, 51, 52, 53, 54, 55, 56]
# ]
# n=0
# for i in range(len(ss)):
#     for j in range(12):
#         n+=ss[i][j]
# print(n)
# #то же самое но одной строчкой
# print(sum(sum(row) for row in ss))
