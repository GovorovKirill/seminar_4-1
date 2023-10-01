print('введите длину первого списка')
n = int(input())
print('введите длину второго списка')
m = int(input())
arr_1 = []
arr_2 = []
arr_3 = []

print('введите элементы первого списка')
for i in range(n):
    arr_1.append(int(input()))

print('введите элементы второго списка')
for j in range(m):
    arr_2.append(int(input()))

i = 0

while i < n:
    j = 0
    while j < m:
        if arr_1[i] == arr_2[j]:
            arr_3.append(arr_2[j])
            j += 1
        else:
            j += 1
    i += 1

arr_4 = list(set(arr_3))
arr_4.sort()

print(f'числа {arr_4} встречаются в обоих списках')

