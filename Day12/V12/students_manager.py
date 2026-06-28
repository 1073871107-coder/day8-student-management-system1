def judge_score():
    while True:
             try:
                score=float(input("请输入学生成绩："))
                return score
             except:print("请输入数字")

def add_students(students):#定义添加学生信息函数
    n=int(input("请输入需要添加的学生数量："))#确定下一步循环次数
    for i in range(n):#把学生信息循环加入students列表
        print(f"请输入第{i+1}位学生的信息：")
        name=input("请输入学生姓名：")
        while True:
             try:
                age=int(input("请输入学生年龄："))
                break
             except:print("请输入数字")
        score=judge_score()
        students.append({
            "姓名":name,
            "年龄":age ,
            "成绩":score
             })
    return students#返回students列表

def print_students(student):
    for k,v in student.items():
        print(f"{k}:{v}")

def none_students(students):
    if not students:
        print("学生信息是空")
        return True
    return False

def show_students(students):#定义显示学生信息函数
    if none_students(students):
       return
    print("学生信息是：")
    for i,student in enumerate(students):#从students列表里取出元素，取出的元素student是字典
        print(f"第{i+1}位同学：")
        print_students(student)

def check_students(students):#定义查找学生信息函数
    if none_students(students):
       return

    name=input("请输入需要查找的学生姓名")
    found=False
    for student in students:
        if student["姓名"]==name:
            print("你查找的学生信息是：")
            print_students(student)
            found=True
            break
    if not found:
        print("没有找到该学生")

def update_students(students):#定义修改学生成绩函数
    if none_students(students):
       return

    name=input("请输入需要修改的学生姓名")
    found=False
    for student in students:
        if student["姓名"]==name:
            score=judge_score()
            student["成绩"]=score
            print("修改后学生信息是：")
            print_students(student)
            found=True
            break
    if not found:
        print("没有找到该学生")
    return students

def del_students(students):#定义删除学生信息函数
    if none_students(students):
       return

    name=input("请输入需要删除的学生姓名")
    found=False
    for i,student1 in enumerate(students):
        if student1["姓名"]==name:
           student=students.pop(i)
           print("删除成功")
           print("删除学生信息是：")
           print_students(student)
           found=True
           break
    if not found:
        print("没有找到该学生")
    return students

def avg_students(students):#定义分数平均数函数
    if none_students(students):
       return

    total_score=0
    for student in students:
        score=student["成绩"]
        total_score+=score
    print(f"平均成绩是:{total_score/len(students)}")