'''Dihedral groups

'''

import string

class Dihedral(object):

    def __init__(self, n):
        assert(1 <= n <= 26)
        self.n = n
        self.state = list(string.uppercase[:self.n])

    def __repr__(self):
        return ' '.join(self.state)

    def alpha(self, n=0):
        assert(0 <= n < self.n)
        tmp = self.state[(self.n-n):]
        tmp.extend(self.state[:(self.n-n)])
        self.state = tmp
        return self

    def beta(self, n=0):
        assert(0 <= n <= 1)
        if n > 0:
            self.state[1:] = reversed(self.state[1:])
        return self

    @classmethod
    def lookup(cls, obj):
        for a in range(obj.n):
            for b in range(2):
                proto = Dihedral(obj.n)
                proto.alpha(a).beta(b)
                print proto.state, obj.state
                if proto.state == obj.state:
                    return ''.join(['A', str(a), 'B', str(b)])

if __name__ == '__main__':
    pass
