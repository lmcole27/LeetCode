class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.head = head
        new_list = []
        for i in range(-1, -len(head)-1, -1):
          # print(i)
          # print(head[i])
          new_list.append(head[i])
          # print(new_list)
        return new_list

head = ListNode(1);
a = ListNode(2);


head = [1,2,3,4,5]


z = Solution().reverseList(head)
print(z)
# print(len(head))
# print(head[-5])

# for i in range(-5,0):
#   print(i)
# head.reverse()
# print(head)

# s = "STRING"
# #x = reversed(s)
# y = list(s)
# y.reverse()
# print(s)
# #print(x)
# print(y)
# #print(z)