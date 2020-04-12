def getHeight(self,root):
        left=0
        right=0
        if root is None:
            return -1
        else:
            left=self.getHeight(root.left)
            right=self.getHeight(root.right)

        if(left>right):
            return(left+1)
        else:
            return (right+1)
        