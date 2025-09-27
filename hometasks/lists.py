numbers = [1,2,3]
numbers1 = list(numbers)
#нельзя numbers1 = numbers, потому что если сделать изменения в numbers1,
# они применятся и на numbers

# text = 'речушка'
# text.replace('у', 'ю')
# print(text)
# text1 = text.find('чf')
# print(text1)

#9.84
# n = input()
# for i in range(len(n)-1):
#     if n[i]==n[i+1]:
#         print(f'numbers are {i} and {i+1}')
#         break
# else:
#     print('no such symbols')


#9.85
# text = input()
# for i in range(len(text)-1):
#     if text[i]=='щ' and text[i+1]=='у':
#         print(i, i+1)
#         break
#     elif text[i]=='ч' and text[i+1]=='у':
#         print(i, i+1)
#         break
# else:
#     print('not found')

#9.86
# text=input()
# for i in range(len(text)-1):
#     if (text[i] == 'ж' and text[i + 1] == 'ы') or (text[i]=='ш' and text[i+1]=='ы'):
#         print('ошибка в написании жи ши')
#         break
# else:
#     print('ошибок в написании жи ши нет')

#9.87
# text = input()
# new_text = text.replace('чя', 'ча').replace('щя', 'ща')
# if new_text == text:
#     print('ошибок нет')
# else:
#     print(new_text)


#9.88
# text = input()
# text1=text.split(',')
# if len(text1) > 1:
#     print(text1[1])
# else:
#     print(text)

#9.89
# text = input().lower()
# if text.find('с')<text.find('т'):
#     print('с стоит раньше чем т')
# else:
#     print('т стоит раньше чем с')

#9.105
# n=input()
# n1=list(n)
# n1[2:9]= n1[2:9][::-1]
# print(",".join(n1))

#9.147


#9.148
# text = 'gdhdf123d gfgh7dhf7987897dshfdghf1'
# count=0
# max=0
# for i in text:
#     if i.isdigit():
#         count +=1
#         if count>max:
#             max=count
#     else:
#         count=0
# print(max)


#9.182
# sentence1 = "это первое предложение и оно длинное"
# sentence2 = "это второе предложение короткое"
# words1 = sentence1.split()
# words2 = sentence2.split()
# unique1=[]
# unique2=[]
# for i in words1:
#     if i not in words2:
#         unique1.append(i)
# for i in words2:
#     if i not in words1:
#         unique2.append(i)
# # ЕЩЕ ОДИН ВАРИАНТ
# # unique_in_1 = [w for w in words1 if w not in words2]
# # unique_in_2 = [w for w in words2 if w not in words1]
# result = unique1 + unique2
# print(result)

#11.6
# n=[]
# for i in range(1,13):
#     n.append(i)
# print(n)

#11.7
# n=[]
# for i in range(20,0,-1):
#     n.append(i)
# print(n)

#11.12
# n=[]
# for i in range (300, 10000000):
#     if (i%13==0 or i%17==0):
#         n.append(i)
#         if len(n) == 20:  # как только нашли 20 — стоп
#             break
# print(n[:20])

#11.60
#n=[1,2,3,4,5,21,22,23,24,25,26]
# count=0
# for i in range(len(n)):
#     if n[i]>20:
#         count+=n[i]
# if count > 100:
#     print('больше сотки')
# else:
#     print('меньше сотки')


#11.63
# n=[1,2,3,4,5,21,22,23,24,25,26]
# count=0
# for i in range(len(n)):
#     if n[i]>50:
#         count+=n[i]
# if count%2==0:
#     print('четное')
# else:
#     print('нечетное')


#11.102
# n=[1,2,3,5,3,6,4]
# n1=sorted(n)
# pair=[]
# for i in range(len(n1)-1):
#     if n1[i]==n1[i+1]:
#         pair.append(n1[i])
#         pair.append(n1[i+1])
# print(pair)


#11.103
# n = [10, -4, 12, 56, -4, -89]
# count = 0
# for i in range(len(n) - 1):
#     # если произведение соседних элементов отрицательное — значит знак поменялся
#     if n[i] * n[i + 1] < 0:
#         count += 1
# print(f"Знак меняется {count} раз(а)")

#11.104
# n=[9,8,8,7,6,4,4,3,2,0,0]
# same=1
# count=0
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         count+=2
#     elif n[i] != n[i+1]:
#         same+=1
# print(count)
# print(same)



#11.105
# n=[0,0,1,2,3,4,5,6,6,7,8,8,8,8,9,13,46,46]
# count=1
# for i in range(len(n)-1):
#     if n[i] != n[i+1]:
#         count+=1
# print(count)

#11.115
# speeds = [
#     180, 200, 190, 220, 210, 230, 240, 250, 180, 200,
#     195, 210, 205, 225, 215, 235, 245, 255, 260, 270,
#     175, 185, 195, 205, 215, 225, 235, 245, 255, 265,
#     180, 200, 190, 210, 220, 230, 240, 250, 260, 270
# ]
# speeds1=max(speeds)
# first=speeds.index(speeds1)+1
# print(first)
# indeces=[]
# for i in range(len(speeds)):
#     if speeds[i] == speeds1:
#         indeces.append(i)
# print(indeces)



#11.145
# n = [1, 2, 3, 4, 5, 6]
# mid = len(n) // 2
# first = n[:mid]   # от начала до mid (не включая mid)
# second = n[mid:]  # от mid до конца
# n1=second+first
# print(n1)

# n = [1, 2, 3, 4, 5, 6]
# mid = len(n)
# for i in range(0,mid,2):
#     n[i], n[i+1]=n[i+1], n[i]
# print(n)


#11.158
n=[1,2,3,4,5,2,6,3]
n1=[]
for i in n:
    if i not in n1:
        n1.append(i)
print(n1)