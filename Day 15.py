 #Complete this method
    def insert(self,head,data): 
            n=Node(data)
            current=head
            temp=head
            if head:
                while current.next:
                    current=current.next
                current.next=n
                return temp
            else :
                head=n
                return head