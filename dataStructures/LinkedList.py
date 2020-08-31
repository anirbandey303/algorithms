## Linked List Data Structutre
## Asymptotic computational complexity
## indexing O(n)
## Insert/Delete at first O(1)
## Insert/Delete at Last O(n)
## Insert/Delete at anywhere in middle O(n)

class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insert_at_first(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if(self.head == None):
            print("LinkedList empty")
            return
        else:
            itr = self.head
            MyList = ''
            while itr:
                #print(itr.data,"-->",end='',sep='')
                MyList = MyList + str(itr.data) + '-->'
                itr = itr.next
            print(MyList)
    
    def insert_at_end(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        else:
            itr = self.head
            while (itr.next != None):
                itr = itr.next
            itr.next = node
            
    def insert_list_of_values(self, list_of_data):
        self.head = None
        for i in list_of_data:
            self.insert_at_end(i)
            
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count
    
    def remove_at(self,position):
        if(position < 0 or position >= self.length()):
            raise Exception("Invalid index")
        if(position == 0):
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if(count == position-1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count + 1
        '''while itr:
            count = count + 1
            previous = itr
            itr = itr.next
            if(position == count):
                break
        
        previous.next = itr.next
        itr = None'''
        

if __name__ == '__main__':
    ll = LinkedList()
    #ll.insert_at_first(10)
    #ll.insert_at_first(5)
    #ll.insert_at_end(15)
    ll.insert_list_of_values([1,2,4,5,6,77,88,544,657])
    ll.remove_at(3) #4th poaition in list, since it starts from zero here. So, 5 must be removed
    ll.print()
    print("Length of linkedList = ", ll.length())