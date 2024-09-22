import os
import time
VERSION = open("VERSION", "r", encoding="utf-8").read()

print("当前版本: " + VERSION)
print("本软件与核桃编程毫无关系")
print("祝您使用愉快！")
print("😋")
time.sleep(3)
#start

os.system("cls")
print("欢迎使用hetaobb工具")
print("请输入要执行的命令:")
print("1. 查看版本")
print("2. 查看帮助 (这是死循环;) )")
print("3. 执行hello world")
print("4. 退出")

#?
while True:
    command = input("请输入要执行的命令:")
    if command == "1":
        print("当前版本: " + VERSION)
    elif command == "2":
        print("帮助:")
        print("1. 查看版本")
        print("2. 查看帮助")
        print("3. 执行hello world")
        print("4. 退出")
    elif command == "3":
        os.system("cls")
        os.system("start helloworld/HelloWorldpython.exe")#python
        #os.system("java -jar helloworld(all)/HelloWorld.jar")#java
        os.system("start helloworld/HelloWorldcpp.exe") #cpp
        
                




