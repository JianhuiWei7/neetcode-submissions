class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}

        # 第一次遍历：创建所有新节点
        current = head
        while current:
            copies[current] = Node(current.val)
            current = current.next

        # 第二次遍历：连接新节点的指针
        current = head
        while current:
            new_node = copies[current]
            new_node.next = copies[current.next]
            new_node.random = copies[current.random]
            current = current.next

        return copies[head]