#NewYoutuber
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:41:49 2020

@author: glori
"""

from stack import push_f
from Ratio23tree import t

class Youtuber:
    def __init__(self):
        self.name = ''
        self.member = 0
        self.Subscribers = 0

MAX = 10
cq = [Youtuber()] * MAX
front = MAX - 1
rear = MAX - 1
tag = 0 #當tag為0時,表示沒有存放資料,若為1,則表示有存放資料


def init_f():
    global rear
    global MAX
    
    name = ['a','b','c','d','e']
    Subscribers = [222,333,555,444,888]
    member = [11,99,55,66,33]
    
    for i in range(5):
        rear = (rear + 1) % MAX
        ptr = Youtuber()
        ptr.name = name[i]
        ptr.Subscribers = Subscribers[i]
        ptr.member = member[i]
        cq[i] = ptr
        push_f(ptr.name,ptr.Subscribers)
        t(ptr.member,ptr.Subscribers)
    
# 新增函數
def enqueue_f():
    global MAX
    global cq
    global front
    global rear
    global tag
    
    while True:    
        if front == rear and tag == 1: #當佇列已滿,則顯示錯誤
            print('\n 此佇列已滿!')
            return False
        else:
            name = input('\n請輸入Youtuber的名字:')
            if search_name(name) == True:
                print('不可以輸入已存在的Youtuber')
                return False
            elif search_name(name) == False:
                try:
                    Subscribers = int(input('\n請輸入Youtuber的訂閱人數:'))
                    member = int(input('\n請輸入Youtuber的會員人數:'))
                    if member > Subscribers:
                        print('會員人數不可大於訂閱人數')
                        return False
                    else:
                        rear = (rear + 1) % MAX
                        ptr = Youtuber()
                        ptr.name = name
                        ptr.Subscribers = Subscribers
                        ptr.member = member
                        cq[rear] = ptr
                        if front == rear:
                            tag = 1
                            print()
                        push_f(ptr.name,ptr.Subscribers)
                        t(ptr.member,ptr.Subscribers)
                except ValueError:
                    print('訂閱人數或會員只能輸入數字')
        return False
# 輸出函數
def list_f():
    global MAX
    global cq
    global front
    global rear
    global tag
   
    count =0
    
    if front == rear and tag == 0:
        print('\n 目前沒有任何 Youtuber !\n')
    else:
        print('\n\n  Youtuber 有下列這些:')
        print('%-15s %-10s %-20s' % ("name", "Subscribers","member"))
        print('************************************')
        i = (front + 1) % MAX
        while i != rear+1:
            print(' ',end='')
            print('%-16s' %cq[i].name,end = '')
            print('%2d' %cq[i].Subscribers,end = '')
            print('%10d' %cq[i].member)
            count += 1
            i = (i + 1) % MAX
        print(' ' ,end = '')
        print('************************************')
        
        print(' 共有%d個 Youtuber\n\n' % count)
        
def search_name(name):
    global cq
    global front
    global rear
    global MAX
    
    i = (front+1) % MAX
    while i != (rear+1) % MAX:
        if name == cq[i].name:
            return True
        else:
            i = (i+1 ) % MAX
    return False