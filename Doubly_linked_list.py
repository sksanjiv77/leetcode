class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = ListNode(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = ListNode(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        if self.head is None:
            new_node = ListNode(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = ListNode(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            
            new_node.prev = cur
            new_node.next = None
            cur.next = new_node
        self.length += 1
    def insert_at_kth_position(self, data, k):
        cur_pos = 0
        cur = self.head
        if k == 0:
            self.insert_at_beginning(data)
        while cur:
            cur = cur.next
            cur_pos += 1
            if cur_pos == k-1:
                if cur.next != None:
                    temp = cur.next   #lost nodes after k
                    new_node = ListNode(data)
                    new_node.prev = cur  
                    new_node.next = temp      
                    cur.next = new_node        
                    temp.prev = new_node
                    return (0, self.length - 1)
                else:
                    return (-1, self.length-1)

    def display_linked_list(self):
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next

        

if __name__ == "__main__":
    d = DoublyLinkedList()
    d.insert_at_end(1)
    # d.insert_at_end(2)
    # d.insert_at_end(3)
    d.insert_at_end(4)
    d.insert_at_end(20)
    d.insert_at_beginning(6)
    # d.insert_at_beginning(5)
    # d.insert_at_beginning(4)
    # d.insert_at_beginning(3)
    # d.insert_at_beginning(2)
    # d.insert_at_beginning(1)
    # d.insert_at_beginning(0)
    rc, max_k = d.insert_at_kth_position(-99, 4)
    if rc == -1:
        print "Insertion at k=4 failed; k cannot be greater than %d" %(max_k)
    d.display_linked_list()


