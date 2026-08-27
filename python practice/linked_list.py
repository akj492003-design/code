class Node :
    def __init__ (self,data,next= None):
        self.data = data 
        self.next = next

class linked_list:
    def __init__(self,head = None):
        self.head = head
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 =self.head
            while(t1.next != None ):
              t1 = t1.next  
            t1.next = temp 
        else:
            self.head = temp
    def print(self):
            t1 =self.head
            while(t1.next != None ):
                print(t1.data)
                t1 = t1.next
            print(t1.data)
                
obj = linked_list()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.print()

        
        

        
        
        
        
         