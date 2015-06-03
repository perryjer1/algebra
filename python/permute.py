'''Permuation group'''


import itertools


class SymmetricGroup:

    def __init__(self, n):
        self.n = n
        self.elements = list(itertools.permutations(range(1,n+1), n))

    def product(self, elem1, elem2):
        assert elem1 in self.elements
        assert elem2 in self.elements
        result = []
        for i in range(len(elem1)):
            result.append(elem2[elem1[i]-1])
        assert tuple(result) in self.elements
        return tuple(result)

    def inverse(self, elem):
        assert elem in self.elements
        for e in self.elements:
            if self.product(e, elem) == self.identity(): return e

    def identity(self):
        return tuple(range(1, self.n+1))

    def pairs(self):
        for pair in itertools.product(self.elements, self.elements):
            yield pair

    def axinva(self, a, x):
        '''Calculate a*x*inverse(a)'''
        assert a in self.elements
        assert x in self.elements
        temp = self.product(a, x)
        temp = self.product(temp, self.inverse(a))
        assert temp in self.elements
        return temp

    def conjugate(self, subset, elem):
        '''Conjugate of {subset} by elem'''
        assert elem in self.elements
        result = []
        for item in subset:
            assert item in self.elements
            result.append(self.axinva(self.inverse(elem), item))
        return tuple(set(result)) # unique

    def conjugacy_class(self, elem):
        assert elem in self.elements
        result = []
        for e, a in itertools.product(self.elements, self.elements):
            if elem == self.axinva(a, e):
                result.append(e)
        return tuple(set(result)) # unique

    def conjugacy_classes(self):
        result = []
        for elem in self.elements:
            result.append(self.conjugacy_class(elem))
        return tuple(set(result)) # unique


def test1():
    s3 = SymmetricGroup(3)
    for pair in s3.pairs():
        print(pair[0], '*', pair[1], '=', s3.product(pair[0], pair[1]))
    print(s3.inverse((3,1,2)))
    print(s3.conjugate([(3,1,2),(3,2,1)], (2,1,3)))
    print(s3.conjugacy_class((3,1,2)))
    print(s3.conjugacy_classes())


def test2():
    s4 = SymmetricGroup(4)
    for pair in s4.pairs():
        print(pair[0], '*', pair[1], '=', s4.product(pair[0], pair[1]))
    print(s4.conjugacy_classes())


if __name__ == '__main__':
    test2()
