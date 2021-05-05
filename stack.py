#訂閱人數

MAX = 10
st = ['']*MAX
top = -1
i = 0


class Subscriber():
    def __init__(self):
        self.name= ''
        self.Subscribers= 0
        


def push_f(name,Subscribers):
    global MAX
    global st
    global top
    global i
    
    if top >= MAX - 1:
        print('\n 堆疊是滿的')
    else:
        ptr = Subscriber()
        ptr.name = name
        ptr.Subscribers = Subscribers
        top += 1
        st[top] = ptr
        i+=1
    return top
    
    
def list_f():
    global st
    global top
    
    #count = 0
    
    if top < 0:
        print('\n沒有紀錄')
    else:
        print('\n\n 顯示訂閱人數')
        print('\n********************************************')
        
        print('%-15s %-10s' % ("姓名", "訂閱人數"))
        print('--------------------------------------------')
        i = top
        while i >= 0:
            print(' ',end = '')
            print('%-16s'%st[i].name,end ='')
            print('%3d'%st[i].Subscribers)
            #count += 1
            i -= 1
            
        print('\n********************************************')
        #print('共有%d筆資料。\n' % count)
    print()
    