#video
from NewYoutuber import search_name
from binarytree import removing,access
from AVL import insert
from heap import iinsert

class Youtuber:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.type = ''
        self.like = 0
        self.view = 0
        self.next = None
        
ptr = None
current = None
prev = None

head = Youtuber()
head.next = head
del_like = ()


def insert_f():
    global head
    global ptr
    global current
    global prev
    global count
    
    ptr = Youtuber()
    print('\n\n******新增VIDEO******')
    ptr.name = input('請輸入youtuber的名字:')
    #錯誤處理--該youtuber需存在
    if search_name(ptr.name) == False:
        print('此youtuber不存在')
        return
    ptr.score = int(input('請輸入此影片之編號:'))
    if search(ptr.score) != None:
        print('此編號的影片已存在')
        print()
        return
    ptr.type = input('請輸入此影片之影片類型:')
    ptr.like = int(input('請輸入此影片之按讚數:'))
    ptr.view = int(input('請輸入此影片之觀看次數:'))
    print('\n************************\n')
    prev = head
    current = head.next
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr
    
    access(ptr.name,ptr.score,ptr.view)
    insert(ptr.type,ptr.like)
    iinsert(ptr.score,ptr.like)

    
    
def search(target):
    global prev
    prev = head
    current = head.next
    
    while current != head:
        if target == current.score:
            return current
        else:
            current = current.next
    return None
    
def delete_f():
    global head
    global current
    global prev
    
    del_score = ''    
    
    if head.next == head:
        print('\n 查無影片')
    else:
        print('\n\n****** Delete Node ******\n')
        del_score = int(input('請輸入影片編號: '))
        
        prev = head
        current = head.next
        while current != head and del_score != current.score: #判斷有沒有找到
            prev = current
            current = current.next        
        if current != head: #有找到
            prev.next = current.next
            current = None
            print(' 影片 %s 已刪除' % del_score)
        else: #找完一圈沒有找到(current = head)
            print(' 查無 %s 之影片' % del_score)
    print('\n****************************\n')
    
def display_f():
    global head
    global current
    
    count = 0
    
    if head.next == head:
        print('\n 沒有紀錄')
    else:
        abc_f()
        print('\n\n****** Display Node ******\n')
        print('%-5s %-5s %-5s %-5s %-5s' % ("NAME","影片編號","影片類型","按讚數","影片觀看次數"))
        print('-----------------------------------------------')
        current = head.next
        while (current != head):
            print('%-8s %-8s %-8s %-7s %-7s' % (current.name, current.score, current.type, current.like, current.view))
            count += 1
            current = current.next
        print('-----------------------------------------------')
        print(' 共有 %s  部影片' % count)
    print('\n******************************\n')
           
def abc_f(): 
    global head
    global current
    
    x=[]
    current = head.next
    while current != head: #從高到低分排
       if x == []:
           x.append([current.name,1,[current.score]])
       else:
           for i in range(len(x)):
               if x[i][0] == current.name:
                   x[i][1] += 1
                   x[i][2].append(current.score)
                   break
               elif i == len(x)-1:
                   x.append([current.name,1,[current.score]])
       current = current.next
    print(x)
    
def def_ff(name): 
    global head
    global current
    
    x=[]
    current = head.next
    while current != head: #從高到低分排
       if name == current.name:
           x.append([current.score,current.like])
       current = current.next
    return x
    
def modify_f(): #找到之後抽掉(delete)再插回去(insert)
    global head
    global current
    global prev
    global ptr
    global del_view
    
    if head.next == head:
        print('\n 沒有紀錄 !!\n')
    else:
        print('\n\n******* Modify Node *******')
        modify_score = int(input('請輸入影片編號: '))
                
        #delete
        prev = head
        current = head.next
        while current != head and modify_score != current.score:
            prev = current
            current = current.next
            
        del_view = current.view
        #兩種情況    
        if current != head: #找到要修改的資料，顯示該筆資料的原始資料
            prev.next = current.next #把舊資料刪除             
             #重新加入新的資料
            newview = int(input('請輸入新的影片觀看次數:'))
            ptr = Youtuber()
            ptr.next = None
            ptr.name = current.name
            ptr.score = current.score
            ptr.type = current.type
            ptr.view = newview
            ptr.like = current.like
            current = None
            
            prev = head
            current = head.next
            while current != head and current.score >= ptr.score: #從高到低分排
               prev = current #prev指向current
               current = current.next #current指向下一個 
            #把車廂掛進鏈結串列    
            ptr.next = current 
            prev.next = ptr
            
            removing(ptr.name,ptr.score,del_view)
            access(ptr.name,ptr.score,ptr.view)
        else:
            print('\n 查無 %s 之影片!\n' % modify_score)