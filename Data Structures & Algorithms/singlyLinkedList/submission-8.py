class LLNode:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    
    def __init__(self):
        # initialize an empty linked list.
        self.head = None
    
    def get(self, index: int) -> int:
        # return the value of the ith node (0-indexed). If the index is out of bounds, return -1
        # index out of bounds
        if index < 0 or not self.head:
            return -1

        i = 0
        cnode = self.head
        while i < index and cnode.next:
            cnode = cnode.next 
            i += 1
        
        # index out of bounds
        if i < index:
            return -1
        return cnode.value

    def insertHead(self, val: int) -> None:
        # insert a node with val at the head of the list
        node = LLNode()
        node.value = val

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
        print(self.getValues())

    def insertTail(self, val: int) -> None:
        # insert a node with val at the tail of the list
        node = LLNode()
        node.value = val

        if not self.head:
            self.head = node
            return
         
        cnode = self.head
        while cnode.next != None:
            cnode = cnode.next
        
        cnode.next = node
        print(self.getValues())

    def remove(self, index: int) -> bool:
        cnode = self.head
        if index < 0 or not self.head or (index == 1 and not self.head.next):
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        
        i = 0
        while i < index-1 and cnode.next:
            cnode = cnode.next
            i += 1
        print('i: ',i)

        if i < index-1:
            return False
        
        else:
            # check if we are removing last node:
            if cnode and cnode.next and cnode.next.next:
                cnode.next = cnode.next.next
            else:
                cnode.next = None
            return True
        print(self.getValues())

    def getValues(self) -> List[int]:
        # return an array of all the values in the linked list, ordered from head to tail
        if not self.head:
            return []

        arr = []
        cnode = self.head
        arr.append(cnode.value)
        while cnode.next != None:
            cnode = cnode.next
            arr.append(cnode.value)
        return arr
        print(self.getValues())