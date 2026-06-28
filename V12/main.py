from file_manager import *
from students_manager import *
def main():#定义主菜单函数
    students=load_data()
    if type(students)!=list:
       students=[]
    while True:
            print("添加学生信息请输入数字：1")
            print("查看学生信息请输入数字：2")
            print("查找学生信息请输入数字：3")
            print("修改学生信息请输入数字：4")
            print("删除学生信息请输入数字：5")
            print("查看平均分请输入数字：6")
            print("结束请输入数字：0")
            n=int(input("请输入数字："))
            if n==1:
               students=add_students(students)
               save_data(students)
            elif n==2:
                show_students(students)
            elif n==3:
                check_students(students)
            elif n==4:
                students=update_students(students)
                save_data(students)
            elif n==5:
                students=del_students(students)
                save_data(students)
            elif n==6:
                avg_students(students)
            elif n==0:
                break    
if __name__=="__main__":
   main()