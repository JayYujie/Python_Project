class FindMinAndMax:

    def __init__(self):
        self.li = [1, 2, 3, 4, 5, 2, 0, 8, 0, 9];
        pass

    def findMin(self):
        minval = 0
        for val in self.li:
            if val <= minval:
                minval = val
        print(minval)
        return minval

    def finMax(self):
        maxval = 0
        for val in self.li:
            if val > maxval:
                maxval = val
        print(maxval)
        return maxval

    def findMinAndMax(self):
        minval = 0
        maxval = 0
        for val in self.li:
            if val > maxval:
                maxval = val
            elif val <= minval:
                minval = val
        tuples = (minval, maxval)
        print(tuples)
        return  tuples
