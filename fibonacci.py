'''
Ciąg Fibonacciego
Autor: Jarosław Drzeżdżon
Data: 1.10.2021 
'''

import math as m

def fib(n):
    a = 0
    b = 1
    if n == 0: return 0
    if n == 1: return 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c

def golden_number(eps):
    prev = fib(2) / fib(1)
    next = fib(3)/ fib(2)
    # print('Dokladność: {:.10f}'.format(eps))
    # print('Prev: {:.10f}'.format(prev))
    # print('Next: {:.10f}'.format(next))
    i = 4
    while abs(next - prev) > eps:
        prev = next
        i += 1
        next = fib(i)/fib(i-1)
        # print('Next: {:.10f}'.format(next))

    return next


for i in range(11):
    print(i,fib(i))

for i in range(2,15):
    print(fib(i) / fib(i-1))

print('liczba złota: ', golden_number(0.00001))
