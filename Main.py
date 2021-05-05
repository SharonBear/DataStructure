#main
import NewYoutuber
import AVL
import heap
import sys
import stack
import Ratio23tree
import video
import binarytree
import Mway

def main():
        
    NewYoutuber.init_f()
    
    option=''
    
    while True:
        print('\n********************************************')
        print('         <1> 新增 YOUTUBER         ')
        print('         <2> Show YOUTUBER         ')
        print('         <3> 新增 VIDEO         ')
        print('         <4> Show VIDEO          ')
        print('         <5> 顯示YOUTUBER訂閱人數         ')
        print('         <6> 顯示YOUTUBER的會員比例排行      ')
        print('         <7> 哪種類型影片獲得最多的按讚數       ')
        print('         <8> 哪部影片獲得最多的按讚數(全部)     ')
        print('         <9> 哪部影片按讚次數最多(同一youtuber) ')
        print('         <10> 修改觀看次數 & SHOW                ')
        print('         <11> Exit                            ')
        print('********************************************')
        
        try:
            option = int(input('輸入選擇 : '))
            if option == 1:
                NewYoutuber.enqueue_f()
            elif option == 2:
                NewYoutuber.list_f()
            elif option == 3:
                video.insert_f()
            elif option == 4:
                video.display_f()
            elif option == 5:
                stack.list_f()
            elif option == 6:
                print('顯示YOUTUBER的會員比例排行')
                Ratio23tree.tt()  
            elif option == 7:
                AVL.list_f()  
            elif option == 8:
                heap.display_f()
            elif option == 9:
                Mway.insert_f()
                Mway.display_f()
            elif option == 10:
                video.modify_f()
                binarytree.show_f()
            elif option == 11:
                sys.exit(0)
                

            else:
                print('不是正確的選項')
                print('重試一次\n')

        except ValueError:
            print('不是正確的選項!')
main()