#ratio23
#會員比例

class Node(object):
    def __init__(self, key):
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None
    def isLeaf(self):
        return self.left is None and self.middle is None and self.right is None
    def isFull(self):
        return self.key2 is not None
    def hasKey(self, key):
        if (self.key1 == key) or (self.key2 is not None and self.key2 == key):
            return True
        else:
            return False
    def getChild(self, key):
        if key < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key < self.key2:
            return self.middle
        else:
            return self.right

class two_three_Tree:
    def __init__(self):
        self.root = None
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self._get(self.root, key)
    def _get(self, node, key):
        if node is None:
            return None
        elif node.hasKey(key):
            return node
        else:
            child = node.getChild(key)
            return self._get(child, key)
    def put(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            pKey, pRef = self._put(self.root, key)
            if pKey is not None:
                newnode = Node(pKey)
                newnode.left = self.root
                newnode.middle = pRef
                self.root = newnode
    def _put(self, node, key):
        # 不重复的key
        if node.hasKey(key):
            return None, None
        # 叶节点，直接插入
        elif node.isLeaf():
            return self._addtoNode(node, key, None)
        # 遍历子树，直到遇到叶节点
        else:
            child = node.getChild(key)
            pKey, pRef = self._put(child, key)
            # 有 pKey, pRef 表示进行了分割
            # pKey 表示往上移的key
            # pRef 表示newnode
            # 每次 _addtoNode 到一个 3-Node的时候,肯定会有pKey和pRef(因为需要分割上移)
            if pKey is None:
                return None, None
            else:
                return self._addtoNode(node, pKey, pRef)
    def _addtoNode(self, node, key, pRef):
        # 3-Node，分割
        if node.isFull():
            return self._splitNode(node, key, pRef)
        # 2-Node
        else:
            # 放入该node的左边
            if key < node.key1:
                node.key2 = node.key1
                node.key1 = key
                # 如果该node有子树
                if pRef is not None:
                    node.right = node.middle
                    node.middle = pRef
            else:
                node.key2 = key
                if pRef is not None:
                    node.right = pRef
            # pKey, pRef
            return None, None
    def _splitNode(self, node, key, pRef):
        # 这是难点,请对照插入的图例,认真学习
        newnode = Node(None)
        if key < node.key1:
            # x是最小的key，把key1移上去
            pKey = node.key1
            node.key1 = key
            newnode.key1 = node.key2
            if pRef is not None:
                newnode.left = node.middle
                newnode.middle = node.right
                node.middle = pRef
        elif key < node.key2:
            # x是中间的key,把自己移上去
            pKey = key
            newnode.key1 = node.key2
            if pRef is not None:
                newnode.left = pRef
                newnode.middle = node.right
        else:
            # x是最大的key,把key2
            pKey = node.key2
            newnode.key1 = key
            if pRef is not None:
                newnode.left = node.right
                newnode.middle = pRef
        node.key2 = None
        return pKey, newnode
    '''def show(self, node = None):
        if node == None:
            node = self.root 
        print(node.key1, end="")
        if node.key2 != None:
            print(",", node.key2)
        else:
            print()
        if node.left != None:
            self.show(node.left)
        if node.middle != None:
            self.show(node.middle)
        if node.right != None:
            self.show(node.right)
            
    def show2(self, node = None):
        if node == None:
            node = self.root 
        
        if node.right != None:
            self.show2(node.right)
            if node.key2 != None:
                print(node.key2)
                
        if node.middle != None:
            self.show2(node.middle)
            
        if node.left != None:
            print(node.key1)
            self.show2(node.left)
            
        if node.left == None:
            if node.middle ==None:
                if node.left ==None:
                    if node.key2 != None:
                        print(node.key2)
                    print(node.key1)
       '''     
    def show2(self,node =None):
        if node == None:
            node = self.root 
 
        if node.right != None:
            self.show2(node.right)
            if node.key2 != None:
                print(node.key2)
                
        if node.middle != None:
            self.show2(node.middle)
            
        if node.left != None:
            print(node.key1)
            self.show2(node.left)
            
        if node.left == None:
            if node.middle ==None:
                if node.left ==None:
                    if node.key2 != None:
                        print(node.key2)
                    print(node.key1)

T = two_three_Tree()        
def t(member,Subscribers):
    a = member/ Subscribers
    
    T.put(a)
def tt():
    T.show2()