import itertools

class Fib:    

    class _Fib_iter:
        def __init__(self):
            self.i = 0
            self.fibs=[]
            self.fibs.insert(0,1) 
            self.fibs.insert(1,1)

        def __next__(self):
                j = self.i
                self.i += 1
                self.fibs.insert(j+2, self.fibs[j+1]+self.fibs[j])
                return self.fibs[j]

    def __iter__(self):
        return Fib._Fib_iter()

fi = Fib()
for f in itertools.islice(fi, 300):
    print(f)
