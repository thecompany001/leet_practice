class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def invertTree(self, root):



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def invertTree(self, root):



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def invertTree(self, root):



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def invertTree(self, root):



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def invertTree(self, root):



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class Solution(object):
    def invertTree(self, root):



XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX