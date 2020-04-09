# Write your code here
class Solution:
    
    def __init__(self):
        self.stack, self.queue = [], []
    def pushCharacter(self,a):
        self.stack.append(a)
    def popCharacter(self):
        return self.stack.pop()
    def enqueueCharacter(self,a):
        self.queue.append(a)
    def dequeueCharacter(self):
        return self.queue.pop(0)