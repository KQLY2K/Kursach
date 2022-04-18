# Башни
# https://codeforces.com/problemset/problem/37/A

t=int(input())
x=list(map(int,input().split()))  #преобразуем строку цифр с разделителем пробел в список чисел
y=set(x) #множетсво элементов из х
a=[]
for i in y:
    a.append(x.count(i)) #добавляем количетсво подстрок i из y в списке x
print(max(a),len(set(x))) #выводим максимальны элемент и длину множества х