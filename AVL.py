# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:58:25 2020

@author: glori
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:45:35 2020

@author: user
"""
#類型按讚數

class Film:
    def __init__(self):
        self.type = ''
        self.likes = 0
        self.bf = 0
        self.llink = None
        self.rlink = None
        
root = None
ptr = None
current = None
prev = None
pivot = None
pivot_prev = None
nodecount = 0

def insert(type_t,likes_t):
    global nodecount
    
    nodecount += 1
    if modify_f(type_t, likes_t) == False:
        sort_f(type_t, likes_t)
    
def sort_f(type_t, likes_t):
    global ptr
    global root
    global current
    global prev
    global pivot
    
    
    op = 0
    current = root
    
    while current != None and likes_t != current.likes:
        if likes_t < current.likes: #插入資料小於目前位置，則往左移
            prev = current
            current = current.llink
        else: #若大於目前位置，則往右移
            prev = current
            current = current.rlink
    #找到插入位置，無重複資料存在
    if current == None or likes_t != current.likes:
        ptr = Film() #配置記憶體
        ptr.type = type_t
        ptr.likes = likes_t
        ptr.llink = None
        ptr.rlink = None
        if root == None:
            root = ptr
        elif ptr.likes < prev.likes:
            prev.llink = ptr
        else:
            prev.rlink = ptr
        bf_count(root)
        pivot = pivot_find()
        if pivot != None: #PIVOT存在，則需改善為AVL-TREE
            op = type_find()
            if op == 11:
                type_ll()
            elif op == 22:
                type_rr()
            elif op == 12:
                type_lr()
            elif op == 21:
                type_rl()
        bf_count(root) #重新計算每個節點的BF值
        
    
                
def bf_count(trees):
    if trees != None:
        bf_count(trees.llink)
        bf_count(trees.rlink)
        #BF值計算方法為左子樹高減去右子樹高
        trees.bf = height_count(trees.llink) - height_count(trees.rlink)
        
def height_count(trees):
    if trees == None:
        return 0
    elif trees.llink == None and trees.rlink == None:
        return 1
    elif height_count(trees.llink) > height_count(trees.rlink):
        return 1 + height_count(trees.llink)
    else:
        return 1 + height_count(trees.rlink)
    
def pivot_find():
    global root
    global current
    global prev
    global pivot
    global pivot_prev
    global nodecount
    
    current = root
    pivot = None
    
    for i in range(nodecount):
        #當BF值的絕對值小於等於1，則將PIVOT指向此節點
        if current.bf < -1 or current.bf > 1:
            pivot = current
            if pivot != root:
                pivot_prev = prev
        if current.bf > 0: #左子樹的高度較高
            prev = current
            current = current.llink
        elif current.bf < 0: #右子樹的高度較高
            prev = current
            current = current.rlink
            
    return pivot

def type_find():
    global current
    global pivot
    
    op_r = 0
    current = pivot
    for i in range(2):
        if current.bf > 0: #左子樹的高度較高
            current = current.llink
            if op_r == 0:
                op_r += 10
            else:
                op_r += 1
        elif current.bf < 0: #右子樹的高度較高
            current = current.rlink
            if op_r == 0:
                op_r += 20
            else:
                op_r += 2
                
    return op_r #回傳值11,22,12,21分別代表LL,RR,LR,RL
 #LL型
def type_ll():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.llink
    temp = pivot_next.rlink
    
    pivot_next.rlink = pivot
    pivot.llink = temp
    
    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next
        
#RR型
def type_rr():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.rlink
    temp = pivot_next.llink
    
    pivot_next.llink = pivot
    pivot.rlink = temp
    
    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next
        
#LR型
def type_lr():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.llink
    temp = pivot_next.rlink
    
    pivot.llink = temp.rlink
    pivot_next.rlink = temp.llink
    
    temp.llink = pivot_next
    temp.rlink = pivot
    
    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp
        
#RL型
def type_rl():
    global root
    global pivot
    global pivot_prev
    
    pivot_next = pivot.rlink
    temp = pivot_next.llink
    
    pivot.rlink = temp.llink
    pivot_next.llink = temp.rlink
    
    temp.rlink = pivot_next
    temp.llink = pivot
    
    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp


def list_f():
    global root
    
    if root == None:
        print('\n沒有紀錄!!')
    else:
        list_data()
        
#將Node資料以中序方式印出        
def list_data():
    global root
    
    print('\n********** 類型影片按讚數 **********')
    print('%-15s %-10s' % ("類型", "按讚數"))
    print('---------------------------------')
    inorder(root)
    print('---------------------------------')

#中序使用遞迴    
def inorder(trees):
    try:
        inorder(trees.rlink)
        print('%-16s' % trees.type, end = '')
        print('%3d' % trees.likes)
        inorder(trees.llink)
    except BaseException:
        None
        
def delete_f(type):
    global root
    global current
    global prev
    global pivot
    global nodecount
    
    clear = None
    op = 0
    current = root
    
    while current != None and type != current.type:
        if type < current.type:
            prev = current
            current = current.llink
        else:
            prev = current
            current = current.rlink
    if current != None and type == current.type:
        if current.llink == None and current.rlink == None:
            clear = current
            if type == root.type:
                root = None
            else:
                if type < prev.type:
                    prev.llink = None
                else:
                    prev.rlink = None
            clear = None
        else:
            if current.llink != None:
                clear = current.llink
                while clear.rlink != None:
                    prev = clear
                    clear = clear.rlink
                current.type = clear.type
                current.likes = clear.likes
                if current.llink == clear:
                    current.llink = clear.llink
                else:
                    prev.rlink = clear.llink
            else:
                clear = current.rlink
                while clear.llink != None:
                    prev = clear
                    clear = clear.llink
                current.name = clear.name
                current.score = clear.score
                if current.rlink == clear:
                    current.rlink = clear.rlink
                else:
                    prev.llink = clear.rlink
                clear = None
                
def modify_f(type,likes):
    global root
    global current
    
        
    current = root
    while current != None and type != current.type:
        if type < current.type:
            current = current.llink
        else:
            current = current.rlink
    #若找到欲更改資料，則列出原資料，並要求輸入新的資料
    if current != None:
        current.likes = current.likes + likes
        sort_f(current.type,current.likes)
        return True
    else:
        return False