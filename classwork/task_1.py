def fib (x , fib_list = [0,1]):
    if x == len(fib_list):
        print(len(fib_list))
        return fib_list
    else:
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib(x, fib_list)
print( fib(int(input("Введите число"))))
