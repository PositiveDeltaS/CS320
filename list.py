class Nil:
    def __str__(self):
        return 'Nil()'
    def nums(lo, hi):
        return Cons(lo, nums(lo+1, hi)) if lo < hi else Nil()
    def __add__(self, other):     # in class Nil
        return other
    def append(self, other):     # in class Nil
        return other
    def map(self, f):           # in Nil
        return self

    def zipnil(self, s):
        return Nil()
    def zip(self, s):
        return Nil()



class Cons:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def __str__(self):
        return 'Cons(' + str(self.head) + ', ' + str(self.tail) + ')'
    def length(self):
        return 1 + self.tail.length()
    def __add__(self, other):     # in class Cons
        return Cons(self.head, self.tail + other)
    def append(self, other):     # in class Cons
        return Cons(self.head, self.tail.append(other))
    def map(self, f):           # in Cons
        return Cons(f(self.head), self.tail.map(f))

    def zip(self, other):
        return other.zipnil(self)
    def zipnil(other, self):
        return Cons((other.head, self.head) , other.tail.zip(self.tail))

def nums(lo, hi):
    return Cons(lo, nums(lo+1, hi)) if lo < hi else Nil()

def powers2(n):
    return Cons(pow(2, n), powers2(n-1)) if n >= 0 else Nil()

alist = Cons(1, Cons(2, Cons(3, Nil())))
blist = Cons(4, Cons(5, Cons(6, Cons(7, Nil()))))

print(alist)
print(blist)

print(nums(0,6).zip(Nil()))
print(nums(0,6).zip(nums(1,7)))
print(nums(0,6).zip(nums(0,3)))
print(nums(0,3).zip(nums(0,6)))
