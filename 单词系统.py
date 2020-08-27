import os
import re
#by 沧海
#2020年8月23开工
if not os.path.exists('./单词系统'):
    os.mkdir('./单词系统')
os.chdir('./单词系统')
file_name=open('name.txt','a+')
name_txt=''
file_name.close()
count_class=0#分类的数量
def Topics():#菜单函数
     print('''
     **************************
     ***    1.添加单词分类  ***
     ***    2.删除单词分类  ***
     ***    3.显示所有分类  ***
     ***    4.复习          ***
     ***    0.退出程序      ***
     **************************
     ''')
def get_name_txt():
     name_txt=''
     name_txt =open(r'name.txt', 'r').read()
     file_name.close()
def addword_class():#添加分类函数
     while 1:
          print("输入exit退出程序")
          print("请输入分类的名称(txt后缀): ",end = '')
          temp = ''
          name=''
          name=str(input())
          if name =='':
               print("请输入正确格式")
               continue
          get_name_txt()
          if name == 'exit':
               print("正在退出程序！！！")
               break
          file_temp=open(name+'.txt','a+')#用来创建分类文件
          print("创建成功！")
          file_temp.close()
          file_name=open('name.txt','a+')
          file_name.write(','+name)
          file_name.close()
          break
def delword_class():#删除分类函数  
     while 1:
          print("""
          1.删除分类
          2.删除所有分类
          0.退出删除分类程序
          """)
          pattern_del='0'
          pattern_del=input("请输入你需要的模式(数字):")
          if pattern_del=='0':
               break
          elif pattern_del=='2':
               get_name_txt()
               print(name_txt)
               result=re.findall(',([\S][^,]+)',name_txt)
               print(result)
          elif pattern_del=='1':
               get_name_txt()
               name_del=""
               name_del=input("请输入你要删除的分类的名字(输入exit退出): ")
               if name_del=='exit':
                    print("正在退出程序")
                    break
               elif name_del not in name_txt:
                    print("没有此分类哦！")
                    continue       
               print("正在删除")
               os.remove(name_del+'.txt')
               print("删除成功!!!")
          else:
               print("格式错误")
               continue
#########################          
     
Topics()#菜单
get_name_txt()
print(type(name_txt))
pattern = 0
while 1:
     pattern = input("请输入需要的模式(数字): ")
     if pattern =='0':
          exit()
     elif pattern =='1':
          addword_class()
          Topics()
          continue
     elif pattern =='2':
          delword_class()
          Topics()
          continue
     else:
          print("格式错误！！")
          continue
     break


