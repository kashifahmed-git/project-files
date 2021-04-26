# Class and Function
class Sample:
    def __int__(self,n):
        self.n = n

     # def factorial(n):
     #    f = 1
     #    for i in range(1, n + 1):
     #       f = f * i
     #    return print(f)

    def fibonacci(n):
        a = 0
        b = 1
        c = 0
        print(a," ",b)
        for i in range(1,n):
            c = a + b
            a = b
            b = c
            print(c)
            # d=list[c]
            # print(d)


n = int(input("Enter the number :"))

s = Sample
s.fibonacci(n)
