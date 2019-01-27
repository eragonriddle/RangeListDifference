import sys
import argparse

'''
    The combinations of the pairwise elements of lists 
        A [(s1, e1), (s2, e2) ...] 
        B [(s1, e1), (s2, e2) ...] 
    for which A - B is true i.e. all ranges in A that are not in B.
    s: start range
    e: end range
    i: include (list A)
    o: exclude (list B)
'''
VALID_SETS = set([
        (('s', 's'), ('i', 'o')),
        (('e', 'e'), ('o', 'i')),
        (('s', 'e'), ('i', 'i')),
        (('s', 'e'), ('i', 'o')),
        (('e', 's'), ('o', 'i')),
        (('e', 's'), ('o', 'o'))
        ])

class RangeListDifference:
    def __init__(self, list_a, list_b):
        '''
            Combine two lists as a single list of tuples.
            Each tuple contains three values (0, 1, 2)
                0: range value from one of the two lists
                1: 's' for start of range or 'e' for end of range
                2: 'i' for range to be included or 'o' for range to be excluded
        '''
        print(list_a)
        print(list_b)
        self.list_all = []
        for item in list_a:
            self.list_all.append((item[0], 's', 'i'))
            self.list_all.append((item[1], 'e', 'i'))
        for item in list_b:
            self.list_all.append((item[0], 's', 'o'))
            self.list_all.append((item[1], 'e', 'o'))
        self._sort()

    def _sort(self):
        '''
            Sort list on the first element of the tuple i.e. range value
        '''
        self.list_all = sorted(self.list_all, key = lambda x: x[0])

    def valid_ranges(self):
        '''
            E.g.:
            list_a = [ (1, 3), (5, 8) ]
            list_b = [ (2, 4), (6, 8) ]
            list_c = [ (1, 's', 'i'), (2, 's', 'o'), (3, 'e', 'i'), (4, 'e', 'o'), (5, 's', 'i'), (6, 's', 'o'), (8, 'e', 'i'), (8, 'e', 'o') ]
            For pair of elements in list_c check if start or end and part of inclusion range or exclusion range.
            s, s, i, o = include
            s, e, i, i = include
            s, e, i, o = include
            e, s, o, i = include
            e, s, o, o = include
            e, e, o, i = include    
    '''
        #print(self.list_all)
        time_ranges = []
        for i in range(0, len(self.list_all) - 1, 2):
            pair = set([
                ((self.list_all[i][1], self.list_all[i + 1][1]), (self.list_all[i][2], self.list_all[i + 1][2]))
                ])
            if pair.issubset(VALID_SETS):
                value1 = self.list_all[i][0]
                value2 = self.list_all[i + 1][0]
                if value1 != value2:
                    time_ranges.append((value1, value2))

        return time_ranges

def main():
    '''
        Accept command line arguments of two lists of ranges and get difference..
    '''
    parser = argparse.ArgumentParser("Subtract list of ranges")
    parser.add_argument('-a', type=int, nargs='+', default=[], help='unix timestamp pairs for list a')
    parser.add_argument('-b', type=int, nargs='+', default=[], help='unix timestamp pairs for list b')
    args = parser.parse_args()
    rld = RangeListDifference(list(zip(args.a[0::2], args.a[1::2])), list(zip(args.b[0::2], args.b[1::2])))
    print(rld.valid_ranges())


if __name__=='__main__':
    try:
        main()
    except:
        print("Error occurred: {0}".format(sys.exc_info()))
