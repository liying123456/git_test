# leetcode_148 排序 链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 归并排序， 快慢指针

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        利用快慢指针找到中间点，将链表分为两半
        利用归并排序
        merge结果
        :param head:
        :return:
        """
        if head == None or head.next == None:
            return head
        slow = ListNode(0)
        slow.next = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        left_sort = self.sortList(head1)
        right_sort = self.sortList(head2)

        #  这里很重要，需要创建一个起始点，并将该起始点赋值给另一个量new_sort,起到记录七点的作用。
        #  最后返回结果时，是p.next而不是new_sort.next
        p = ListNode(0)
        new_sort = p
        while left_sort and right_sort :
            if left_sort.val < right_sort.val:
                new_sort.next = left_sort
                left_sort = left_sort.next
                new_sort = new_sort.next
            else:
                new_sort.next = right_sort
                right_sort = right_sort.next
                new_sort = new_sort.next
        if left_sort:
            new_sort.next = left_sort
        if right_sort:
            new_sort.next = right_sort
        return p.next
