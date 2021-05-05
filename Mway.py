#Mway
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:29:17 2020

@author: user
"""

#Mway(同一youtuber觀看次數)
from video import def_ff

class Views:
    def __init__(self):
        self.iD = 0 #輸出時識別節點
        self.n = 0 #節點內的鍵值數
        self.key = [0] * 3 #節點鍵值
        self.num = [0] * 3
        self.link = [None] * 3 #節點子鍵值
        #key從1開始編號，link從0開始編號
        
MAX = 3 #設定此為3-Way Tree的最大節點
ptr = None
root = None
node = None
prev = None
parent = None
replace = None
id_seq = ''
nn = ''

def insert_f():
    global nn
    global root
    
    root = None
    
    nn = input('哪個youtuber: ')
    data = def_ff(nn)
    if data == []:
        print('沒有此youtuber的影片紀錄')
    else:
        for i in range(len(data)):
            film_number = data[i][0]
            film_like = data[i][1]
            create(film_like,film_number)
    print()
    
def create(like,number):
    global root
    global ptr
    global node
    global prev
    
    i = 0
    
    if root == None: #樹根為空
        initial()
        ptr.key[1] = like
        ptr.num[1] = number
        ptr.n += 1
        root = ptr
    else:
        search_num(like)
        node = search_node(like,number)#找尋插入點
        if node != None:
            i = 1
            while i < MAX-1:
                if like < node.key[i]:
                    break
                i += 1
            moveright(i, like, number)
        else:
            initial()
            ptr.key[1] = like
            ptr.num[1] = number
            ptr.n += 1
            i = 1
            while i < MAX:
                if like < prev.key[i]:
                    break
                i += 1
            prev.link[i-1] = ptr 
        
def initial():
    global MAX
    global ptr
    
    ptr = Views()
    for i in range(MAX):
        ptr.link[i] = None
    ptr.n = 0
    
def search_num(num):
    global root
    global node
    global prev
    global parent
    
    node = root
    while node != None:
        parent = prev
        prev = node
        i = 1
        done = 0
        while i <= node.n:
            if num == node.key[i]:
                return i #找到num，回傳
            if num < node.key[i]:
                node = node.link[i-1]
                done = 1
                break
            i += 1
        if done == 0:
            node = node.link[i-1] #最右邊的link
    return 0 #沒有找到則回傳0'''

def search_node(like,number):
    global MAX
    global root
    
    node_temp = root
    
    while node_temp != None:
        if node_temp.n < MAX-1: #根結點未滿，放入根節點
            return node_temp 
        else:
            i = 1
            done = 0
            while i < MAX:
                if node_temp.n < i:
                    break
                if like < node_temp.key[i]:
                    node_temp = node_temp.link[i-1]
                    done = 1
                    break
                i += 1
            if done == 0:
                node_temp = node_temp.link[i-1]
    return node_temp 

def moveright(index, like, number):
    global node
    
    i = node.n + 1
    
    while i > index: #資料右移至INDEX處
        node.key[i] = node.key[i-1]
        node.num[i] = node.num[i-1]
        node.link[i] = node.link[i-1]
        i -= 1
    node.key[i] = like #插入NUM
    node.num[i] = number
    #調整NUM左右鏈結
    if node.link[i-1] != None and node.link[i-1].key[0] > like:
        node.link[i] = node.link[i-1]
        node.link[i-1] = None
    node.n += 1
    
def display_f():
    global root
    global id_seq
    global nn
    
    if root == None:
        print('\n沒有紀錄!\n')
    else:
        id_seq = 'a' #節點編號由a開始
        preorder_id(root) #給予每個節點編號
        print('%s youtuber的影片按讚數排行' % nn)
        print('=========================')
        print('%-5s %5s' % ("影片編號","按讚數"))
        inorder_num(root) #輸出節點資料
        print('=========================')

def preorder_id(tree):
    global id_seq
    
    if tree != None:
        tree.iD = id_seq
        id_seq = chr(ord(id_seq) + 1)
        for i in range(tree.n+1):
            preorder_id(tree.link[i])
            
def inorder_num(root):
    global MAX
    
    if root != None:
        if root.link == [None]*MAX:
            for i in range(root.n):
                print('%-10d %-5d' % (root.num[root.n-i],root.key[root.n-i]))
        else:
            for i in range(MAX):
                max_ = MAX-1
                if  i != max_:
                    if root.link[max_-i] != None:
                        inorder_num(root.link[max_-i])
                    print('%-10d %-5d' % (root.num[max_-i],root.key[max_-i]))
                else:
                    if root.link[max_-i] != None:
                        inorder_num(root.link[max_-i])