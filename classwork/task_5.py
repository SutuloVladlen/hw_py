from random import randint
a = list(randint(0,20)for i in range(int (input("длинна 1 списка"))))
print(a)
count =0
for i in range (1,len(a)-1):
    if a[i-1] < a[i] > a[i+1]:
        print (a[i])
        count +=1
print (count)
