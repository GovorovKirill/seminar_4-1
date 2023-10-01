print('введите число кустов')
n = int(input())
arr_1 = []

print('введите число ягод на каждом кусте')
for i in range(n):
    arr_1.append(int(input()))

arr_2 = arr_1[1:] + arr_1[:1]
arr_3 = arr_1[-1:] + arr_1[:-1]

max_harvest = 0

i = 0
j = 0
k = 0

while i < n and j < n and k < n:
    if max_harvest < (arr_1[i] + arr_2[j] + arr_3[k]):
        max_harvest = arr_1[i] + arr_2[j] + arr_3[k]
        i += 1
        j += 1
        k += 1

    else:
        i += 1
        j += 1
        k += 1

print(max_harvest)
