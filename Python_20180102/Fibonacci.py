# 查找斐波纳契数列中第 N 个数。
#
# 所谓的斐波纳契数列是指：
#
# 前2个数是 0 和 1 。
# 第 i 个数是第 i-1 个数和第i-2 个数的和。
# 斐波纳契数列的前10个数字是：
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


class Fibonacci:

    def __init__(self):
        pass

    def fibonacci(self, n) -> int:
        # write your code here
        if n < 2:
            return n
        return self.fibonacci(n - 2) + self.fibonacci(n - 1)

    def nonRecursiveFibonacci(self, n) -> int:
        # 首先定义第0个和第1个数组
        fibVal = [0, 1];
        # 循环体变量 初始化2开始
        count = 2;
        # 目的是为了往数组里插入最新的数值 也就是 有且仅当 数组长度小于或者等于输入的元素个数 进入循环体
        while len(fibVal) <= n:
            # 循环变量每次会累加 当累加到输入元素个数 即进入逻辑运算
            if count <= n:
                pre = fibVal[count - 1]
                nex = fibVal[count - 2]
                # 把数组的前两个元素相加 追加的数组末尾
                fibVal.append(pre + nex)
                # 并且把循环变量累加
                count = count + 1
        # 获取数组长度
        length = len(fibVal)
        # 因为数组下标是0开始即返回长度-1的元素即为所得
        return fibVal[length - 1]

    def nonRecursiveFibonacci2(self, n) -> int:
        if n < 2 and n >= 0:
            return n
        # 首先定义第一个元素和第二个元素 以及默认返回的值val 暂且初始化为0
        first = 0;
        second = 1;
        val = 0;
        # 循环体变量 初始化2开始
        index = 2;
        # 有且仅当 数组长度小于或者等于输入的元素个数 进入循环体
        while index <= n:
            # 迭代值新值变量 为 第一个元素和第二个元素之和
            val = first + second
            # 置换第一元素
            first = second
            # 置换第二元素
            second = val
            # 循环变量累加
            index = index + 1
        return val
