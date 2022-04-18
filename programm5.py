# Шоколадки
# https://codeforces.com/problemset/problem/1139/B

n = int(input()) #кол-во типов шоколадок
a = [int(i) for i in input().split()] # массив шоколадок
count = a[n - 1] #инициализация
for i in range(n - 2, -1, -1): 
    if a[i + 1] - 1 > 0: #проверка на ноль
        a[i] = min(a[i], a[i + 1] - 1) #минимум из двух
        count += a[i] #прибавдяем
    else: break
print(count) #выводим