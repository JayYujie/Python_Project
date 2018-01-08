class YangHui:

    def __init__(self):
        pass

    @staticmethod
    def triangle(length):
        print("YangHui Retangle is :")
        m = []
        for i in range(0,11):
            n = []
            for j in range(i):
                if j == 0 or j == i-1:
                    n.append(1)
                else:
                    n.append(m[j - 1] + m[j])

            print(n)
            m = n
