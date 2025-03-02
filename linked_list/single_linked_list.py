class Node :
    def __init__(self, data, next):
        self.data = data
        self.next = next


class SingleLinkedList :
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data) :
        node = Node(data, self.head)    
        self.head = node

    def print(self) :
        itr = self.head
 
        ll = ""
        while itr :
            ll = ll + str(itr.data) + "-->"

            itr = itr.next

        print(ll)    

    def insert_at_end(self, data) :
        if self.head == None :
            self.head = Node(data, None)
            return
        
        itr = self.head 

        while itr.next :
            itr = itr.next    

        itr.next = Node(data, None)

    def insert_at(self, index, data) :
        if index == 0 :
            self.insert_at_begining(data)
            return
        
        itr = self.head

        count = 0

        while itr :
            if count == index-1 :
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def get_length(self) :
        itr = self.head

        count = 0

        while itr :
            count +=1
            itr = itr.next

        print(count)            




if __name__ == '__main__' :
    ll = SingleLinkedList()
    
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_end(30)
    ll.insert_at(2, "yash")
    ll.print()
    ll.get_length()