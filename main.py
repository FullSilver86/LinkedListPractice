class Node():
    def __init__(self,data):
        self.data = data
        self.nextnode = None

class LinkedList():

    def __init__(self):
        self.head = None

    def add_atfront(self, data):
        self.data = data
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.nextnode = self.head
            self.head = node

    def __repr__(self):
        list = []
        node = self.head
        while node:
            list.append(node.data)
            node = node.nextnode

        return str(list)


    def add_atend(self,data):
        self.data = data
        node = self.head
        while node.nextnode:
            node = node.nextnode
        node.nextnode = Node(data)


    def search(self, data_to_search):
        self.data_to_search = data_to_search
        node = self.head
        index = 1
        while node.data != data_to_search:
            node = node.nextnode
            index += 1
        if not node:
            print("not found")
        else:
            print(f"object {data_to_search} at position {index}")





l1 = LinkedList()
l1.add_atfront(10)
l1.add_atfront(20)
l1.add_atend(300)
print(l1)
l1.search(300)
