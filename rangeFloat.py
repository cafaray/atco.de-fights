class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.i + self.step >= self.stop:
            raise StopIteration        
        else:                        
            self.i+=self.step
            return self.i - self.step            


def rangeFloat(args):
    return list(FRange(*args))

print(rangeFloat([5]))