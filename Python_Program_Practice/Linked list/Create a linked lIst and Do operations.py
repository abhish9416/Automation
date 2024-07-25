class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def insert(self,index,value):
        new_node = Node(value)
        if index <= -1:
            return None
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
    def delete(self,index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None

    def get(self,index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    def set(self,index,value):
        temp = self.get(index)
        while temp is not None:
            temp.value = value
            return True
        return False


    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result = result +str(temp.value)
            if temp.next is not None:
                result = result + '->'
            temp = temp.next
        return result

l1 = Linkedlist()
l1.append(1)
l1.append(2)
l1.append(2)
l1.append(2)
l1.append(2)
l1.insert(2,6)
print(l1)
l1.delete(2)
print(l1)
# l1.set(1,4)


