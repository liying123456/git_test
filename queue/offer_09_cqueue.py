# 剑指 Offer 09. 用两个栈实现队列
# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除
# 整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:
    """
    利用两个栈实现队列功能，
    列表可以模拟栈
    """

    def __init__(self):
        self.A = []  # 添加数据
        self.B = []  # 删除数据

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:  # 当B栈有数据时，pop
            return self.B.pop()
        elif not self.A:  # 当AB栈都为空，即队列为空，返回1
            return -1
        while self.A:  # 当B为空，A有数据时，需要一次性将A的所有数据添加到B中。然后再pop
            self.B.append(self.A.pop())
        return self.B.pop()


# obj = CQueue()
# # value = ["CQueue","appendTail","deleteHead","deleteHead"]
# obj.appendTail(value)
# param_2 = obj.deleteHead()
