# Двустроние строки
# https://codeforces.com/problemset/problem/1506/C

t = int(input()) #Кол-во строк
for _ in range(t):
    a = input() #строка
    b = input() #строка
    l = list() #список
    n = len(b)
    m = len(a)
    for i in range(n):
        for j in range(i+1,n+1):
            l.append(b[i:j]) #с помощью среза добавляем элементы в список
    x = 0
    for i in l:
        y = len(i) #длина элемента в списке
        if((i in a) and (y > x)):
            x = len(i)
    print(n+m-(2*x))