import itertools

class Fib:    

    class _Fib_iter:
        def __init__(self):
            self.a1=1 
            self.a2=1
            
        def __next__(self):
                k = self.a1
                self.a2=self.a1+self.a2
                self.a1=self.a2-self.a1
                return k

    def __iter__(self):
        return Fib._Fib_iter()

fi = Fib()
for f in itertools.islice(fi, 300):
    print(f)
