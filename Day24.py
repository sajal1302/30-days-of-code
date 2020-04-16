def removeDuplicates(self,head):
        #Write your code here
        temp = head
        while temp:
            if temp.next and temp.data == temp.next.data:
                temp2 = temp.next
                temp.next = temp.next.next
                del temp2
            else:
                temp = temp.next
        return head
