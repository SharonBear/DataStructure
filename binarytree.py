#binarytree
#二元樹(修改按讚數)

class Views:
    name = ''
    number = 0
    view = 0
    llink = None
    rlink = None
    
root = None


#搜尋target所在節點        
def search(target):
    global root
    node = root
    while node != None:
        if target == node.view:
            return node
        elif target < node.view: #target小於目前節點，往左搜尋
            node = node.llink
        else: #target大於目前節點，往右搜尋
            node = node.rlink
    return node

            
            
    
def access(name,number,view):
    global root
    node = None
    prev = None

    ptr = Views()
    ptr.name = name
    ptr.number = number
    ptr.view = view
    ptr.llink = None
    ptr.rlink = None
    if root == None: #當根節點為空的狀況
        root = ptr
    else: #當根節點不為空的狀況
        node = root
        #搜尋資料插入點
        while node != None: 
            prev = node
            if ptr.view < node.view:
                node = node.llink
            else:
                node = node.rlink
        if ptr.view < prev.view:
            prev.llink = ptr
        else:
            prev.rlink = ptr
    
def removing(name,number,view):
    global root
    del_node = search(view)
    #節點不為樹葉節點的狀況
    if del_node.llink != None or del_node.rlink != None:
        del_node = replace(del_node)
    else:
        if del_node == root:
            root = None
        else:
            connect(del_node, 'n')
    del_node = None #釋放記憶體

#尋找刪除非樹葉節點的替代節點   
def replace(node):
    re_node = None
    #當右子樹找不到替代節點，會搜尋左子樹是否存在替代節點
    re_node = search_re_r(node.rlink)
    if re_node == None:
        re_node = search_re_l(node.llink)
        
    if re_node.rlink != None: #當替代節點有右子樹存在的狀況
        connect(re_node, 'r')
    elif re_node.llink != None: #當替代節點有左子樹存在的狀況
        connect(re_node, 'l')
    else: #當替代節點為樹葉節點的狀況
        connect(re_node, 'n')
    node.name = re_node.name
    node.number = re_node.number
    node.view = re_node.view
    return re_node

#調整二元搜尋樹的鏈結，link為r表示處理右鏈結，為l表示處理左鏈結，為n則將鏈結指向None
def connect(node,link):
    parent = search_p(node) #搜尋父節點
    if node.view < parent.view: #節點為父節點左子樹的狀況
        if link == 'r': #link為r
            parent.llink = node.rlink
        elif link == 'l': #link為l
            parent.llink = node.llink
        else: #link為n
            parent.llink = None
    #節點為父節點右子樹的狀況
    elif link == 'r': #link為r
        parent.rlink = node.rlink
    elif link == 'l': #link為l
        parent.rlink = node.llink
    else: #link為n
        parent.rlink = None
 
def search_re_l(node):
    re_node = node
    while re_node != None and re_node.rlink != None:
        re_node = re_node.rlink
    return re_node
 
def search_re_r(node):
    re_node = node
    while re_node != None and re_node.llink != None:
        re_node = re_node.llink
    return re_node


#尋找node的父節點
def search_p(node):
    global root
    parent = root
    while parent != None:
        if node.view < parent.view:
            if node.view == parent.llink.view:
                return parent
            else:
                parent = parent.llink
        elif node.view == parent.rlink.view:
            return parent
        else:
            parent = parent.rlink
    return None


def show_f():
    global root
    if root == None:
        print('')
        return
    print('\n==========修改後影片資料(觀看次數)==========')
    print('%-5s %-5s %5s' % ("Youtuber姓名","影片編號","觀看次數"))
    inorder(root)
    print('===========================================')


#以中序法輸出資料，採遞迴方式    
def inorder(node):
    if (node != None):
        inorder(node.rlink)
        print('%-12s %-9d %-5d' % (node.name,node.number,node.view))
        inorder(node.llink)