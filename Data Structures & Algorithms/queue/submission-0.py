class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Deque:
    
    def __init__(self):
        self.beg = None
        self.end = None

    def isEmpty(self) -> bool:
        return self.beg == None and self.end == None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.beg = new_node
            self.end = new_node
        else:
            self.end.right = new_node
            new_node.left = self.end
            self.end = self.end.right    

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.beg = new_node
            self.end = new_node
        else:
            self.beg.left = new_node
            new_node.right = self.beg
            self.beg = self.beg.left

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            value = self.end.value
            if self.end.left:
                self.end = self.end.left
                self.end.right = None
            else:
                self.end = None
                self.beg = None
            return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            value = self.beg.value
            if self.beg.right:
                self.beg = self.beg.right
                self.beg.left = None
            else:
                self.end = None
                self.beg = None
            return value

