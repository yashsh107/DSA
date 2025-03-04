class Node :
    def __init__(self, data, next, pre):
        self.data = data
        self.next = next
        self.pre = pre

class DoubleLinkedList :
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data) :
        node = Node(data, self.head, None)
        self.head = node

    def print(self) :
        itr = self.head

        dll = ""

        while itr :    
            dll = dll + str(itr.data) + "-->"
            itr = itr.next    

        print(dll)        

    def insert_at_end(self, data) :
        if self.head == None :
            node = Node(data, None, None)
            self.head = node
            return

        itr = self.head    
        while itr.next :
            itr = itr.next

        node = Node(data, None, itr)    
        itr.next = node

    def insert_at(self, data, index) :
        if index == 0 :
            node = Node(data, self.head, None)
            self.head = node
            return

        itr = self.head
        count = 0

        while itr :
            if count == index-1 :
                node = Node(data, itr.next, itr)
                itr.next.pre = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def get_lenght(self) :
        if self.head == 0 :
            print(0)
            return

        itr = self.head
        count = 0

        while itr :
            count += 1
            itr = itr.next        

        print(count)    



if __name__ == '__main__' :
    dll = DoubleLinkedList()

    # dll.insert_at_begining(10)
    # dll.insert_at_begining(20)
    # dll.insert_at_begining(30)
    dll.insert_at_end(50)
    dll.insert_at_end(60)
    dll.insert_at_end(70)
    dll.insert_at_end(80)
    dll.insert_at(40, 2)
    dll.print()
    dll.get_lenght()