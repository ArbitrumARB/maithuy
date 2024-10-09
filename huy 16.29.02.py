def selection_sort(a):
    for i in range(0,len(a)-1):
        min_current=i
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
             min_current=j
        a[i],a[min_current]=a[min_current],a[i]


n=int(input('Nhap n='))
a=[]
for i in range(n):
    x=int(input(f'Nhap phan tu thu {i+1} ='))
    a.append(x)
    print(i)

selection_sort(a)
b=a[::-1]



print(b)