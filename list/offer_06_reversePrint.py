# jianzhi offer 06 从尾到头打印链表
# 输入：head = [1,3,2]
# 输出：[2,3,1]
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_list(ls):
    """
    创建链表
    :param ls:
    :return:
    """
    if len(ls) == 0:
        return None
    h = ListNode(ls[0])
    r = h
    for i in ls[1:]:
        point = ListNode(i)
        h.next = point
        h = h.next
    return r


class Solution:

    def reversePrint_1(self, head: ListNode)->[int]:
        """
        利用栈完成列表的倒转
        :param head:
        :return:
        """
        if head is None:
            return []
        l = []
        r = []
        while head is not None:
            l.append(head.val)
            head = head.next
        while(l):
            r.append(l.pop())
        return r

    def reversePrint_2(self, head: ListNode)->[int]:
        """
        利用递归完成列表的翻转
        :param head:
        :return:
        """
        self.r = []
        if head is not None:
            self.reversePrint_2(head.next)
            self.r.append(head.val)
        return self.r


head = [1,2,3]
hea = build_list(head)
sol = Solution()
result = sol.reversePrint_2(hea)
print(result)
