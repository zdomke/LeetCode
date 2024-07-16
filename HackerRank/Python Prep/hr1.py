class Multiset(object):
    def __init__(self):
        self.multiset = {}
        self.length = 0

    def add(self, val: int):
        # adds one occurrence of val from the multiset, if any
        if val in self.multiset:
            self.multiset[val] += 1
        else:
            self.multiset[val] = 1
        self.length += 1

    def remove(self, val: int):
        # removes one occurrence of val from the multiset, if any
        if self.__contains__(val):
            self.multiset[val] -= 1
            self.length -= 1
    
    def __contains__(self, val: int):
        # returns True when val is in the multiset, else returns False
        return val in self.multiset and self.multiset[val] > 0
    
    def __len__(self):
        # returns the number of elements in the multiset
        return self.length

def main():
    m = Multiset()

    m.add(12)
    m.add(12)
    print(m.__contains__(12))
    print(m.__contains__(13))
    print(m.__len__())
    m.add(13)
    m.add(14)
    m.add(14)
    m.add(1)
    m.remove(12)
    m.remove(12)
    print(m.__contains__(12))
    print(m.__contains__(13))
    print(m.__len__())


if __name__ == '__main__':
    main()