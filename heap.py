#heap

MAX = 10
heap_tree = [0] * MAX # Heap陣列
last_index =0#最後一筆資料的index

class film:
    def __init__(self):
        self.likes = 0
        self.name = ''



# 新增函數
def iinsert(name,like):
    global MAX
    global last_index
    if last_index >= MAX-1:#資料數超過上限,顯示錯誤訊息
        print('\n 已達youtuber人數上限10位!' % MAX - 1)
    create(name,like)# 建立Heap

    
def create(film_name,film_likes):
    global last_index
    global heap_tree
    ptr = film()
    ptr.name = film_name
    ptr.likes = film_likes
    last_index += 1
    heap_tree[last_index]= ptr#將資料新增於最後
    adjust_u(heap_tree, last_index)#調整新増資料
    
    
#從下而上調整資料,index為目前資料在陣列之INDEX
def adjust_u(temp, index):
    while (index>1): #將資料往上調整至根為止
        if temp[index].likes<= temp[index//2].likes:#資料調整完畢就跳出,否則交換資料
            break
        else:
            exchange(temp, index, index//2)
        index //= 2
        
#交換傳來之id1及id2儲存之資料
def exchange(arr, id1, id2):
    film_temp = arr[id1]
    arr[id1] = arr[id2]
    arr[id2] = film_temp

# 輸出函數
def display_f():
    global last_index
    option = ''
    
    if last_index< 1:#無資料存在,顯示錯誤訊息
        print('\n 沒有紀錄!!\n')
    else:
        print()
        print('******************')
        print(' <1>遞增排列')#選擇第一項為由小到大排列
        print(' <2>遞減排列')#選擇第二項為由大到小排列
        print('********************')
        while True:
            try:
                option = input('\n輸入選擇: ')
            except ValueError:
                print()
                print('不是正確選項')
                print('再試一次\n')
            if (option == '1' or option == '2'):
                break
        show(option)

#印出資料於螢幕
def show(op):
    global last_index
    global heap_tree
    heap_temp =[]
    tChar =''
    
    #將Heap資料複製到另一個陣列作排序工作
    heap_temp = [i for i in heap_tree]
    #將陣列調整為由小到大排列
    c_index = last_index - 1
    while c_index > 0:
        exchange(heap_temp, 1, c_index+1)
        adjust_d(heap_temp, 1, c_index)
        c_index -= 1
    print('\n%-15s %-10s' % ("影片編號", "按讚數"))
    print('**********************')
    #選擇第一種方式輸出,以遞迴方式輸出一使用堆疊
    #選擇第二種方式輸出,以遞迴方式輸出一使用佇列
    if op == '1':
        for c_index in range(1, last_index + 1):
            print('%-16s' %heap_temp[c_index].name,end = '')
            print('%3d' %heap_temp[c_index].likes)
    elif op == '2':
        c_index = last_index
        while c_index > 0:
            print('%-16s' %heap_temp[c_index].name,end = '')
            print('%3d' %heap_temp[c_index].likes)
            c_index -= 1
    print('*********************')
    print(' 影片數量: ', last_index, '\n')

#從上而下調整資料index1為目前資料在陣列之INDX,index2為最後一筆資料在陣列之INDEX
def adjust_d(temp, index1, index2):
    # film_temp記錄目前資料,index_emp則是目前資料之CHILDRNNOD的INDEX
    film_temp = temp[index1]
    index_temp = index1 * 2
    #當比較資料之INDE不大於最後一筆資料之INDEX,則繼續比較
    while index_temp <= index2:
        if index_temp< index2 and temp[index_temp].likes < temp[index_temp+1].likes:
            index_temp+= 1 #index_temp記録目前資料之CHILDENNODE中較大者
        if film_temp.likes >= temp[index_temp].likes:#比較完畢則跳出,否則交換資料
            break
        else:
            temp[index_temp//2] = temp[index_temp]
            index_temp*= 2
    temp[index_temp//2] = film_temp
'''
# 刪除函數
def delete_f():
    global last_index
    
    film_temp = 0
    del_index = 0
    
    if last_index< 1:#無資料存在・顆示錯誤訊息
        print('\n No member to logout!!')
        print(' Please check again!!')
    else:
        film_temp= int(input('\n Please enter logout ID number: '))
        del_index = search(film_temp)
        if del_index== 0:#沒找到資料,顯示錯課訊息
            print(' ID number not found!!')
        else:
            removes(del_index)#刪除資料,並調整Heap
            print(' ID number ', film_temp, ' logout!!')
            
#尋找陣列中film_temp所在
def search(film_temp):
    global heap_tree
    
    for c_index in range(1, len(heap_tree)):
        if film_temp == heap_tree[c_index]:
            return c_index #找到則回傳資料在陣列中之INDEX
    return 0#沒找到則回傳0
    
#從Heap中刪除資料,INDEX_TEMP為欲刪除資料之INDEX
def removes(index_temp):
    global last_index
    global heap_tree
    
    #以最後一筆資料代替刪除資料
    heap_tree [index_temp] = heap_tree [ last_index]
    heap_tree[ last_index] = 0
    last_index -= 1
    if last_index> 1:#當資料筆數大於1筆,則做調整
        #當替代資料大於其PRENTNOD,則往上調整
        if heap_tree[index_temp] > heap_tree[index_temp//2] and index_temp > 1:
            adjust_u(heap_tree, index_temp)
        else:#替代資料小於其CHILDRENNODE,則往下調整
            adjust_d(heap_tree, index_temp, last_index-1)'''