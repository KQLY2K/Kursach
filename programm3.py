# Уничтожение минимума
# https://codeforces.com/problemset/problem/1607/C

for z in range(int(input())):
    n=int(input()) # вводим кол-во элементов
    a=list(map(int,input().split())) # преобразуем строку цифр с разделителем пробел в список чисел
    if(n==1): #
        print(a[0])
        continue
    else:
        a.sort() #
        m=a[0]
        for i in range(len(a)-1):
            m=max(a[i+1]-a[i],m) # выполняем минимум
        print(m) #вывод