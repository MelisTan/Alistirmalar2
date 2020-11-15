# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7
# fib(7) = fib(6) + fib(5)
# Bu program ilk 30 fibinacci sayısını bularak ekrana yazdırmaktadır.
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(31):
    print(fibonacci(i) , end= " ")
