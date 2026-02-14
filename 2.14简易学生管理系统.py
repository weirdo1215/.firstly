students=[{
    "id":1,
    "name":"学生1",
    "age":18,
    "score":90,
},{
    "id":2,
    "name":"学生2",
    "age":19,
    "score":95,
     },{
        "id":3,
        "name":"学生3",
        "age":20,
        "score":100,
    },{
        "id":4,
        "name":"老6",
        "age":18,
        "score":66,
    } ]
"打印提示"
def menu():
    print("\n\033[31m1.显示 2.添加 3.删除 4.更改 5.排序 6.其他键退出\033[0m")
"显示学生"
def showstu():
    for i in students:
        print(i)
"添加学生"
def addstu():
    s={}
    s["id"]=input("请输入id:")
    s["name"]=input("请输入名字:")
    s["age"]=input("请输入年龄:")
    s["score"]=input("请输入分数:")
    students.append(s)
"删除学生"
def delstu():
    del_res=int(input("输入要删除的id:"))
    for i in students:
        if i["id"]==del_res:
            print("找到了学生:",i,"是否删除？1是 2否")
            del_k=input()
            if del_k=="1":
                students.remove(i)
                break
            elif del_k=="2":
                break
            else:
                print("请输入是或1是 2否")
                if(input()=="2"):
                    break
                else:
                    delstu()
"修改学生"
def changestu():
    q=""
    def a():
        print("你要改什么:\033[31mid name age score\033[0m")
        q = input()
        for j in i.keys():
            if j == q:
                if j == "name":
                    i[j] = input("改:")
                    m = input("是否还要改 1.改 2.不改 ")
                    if m == "1":
                        a()
                    elif m == "2":
                        break
                    break
                else:
                    i[j] = int(input("改吧:"))
                    m = input("是否还要改 1.改 2.不改 ")
                    if m == "1":
                        a()
                    elif m == "2":
                        break
                    break
    change=int(input("请输入要更改的学生id:"))
    for i in students:
        if i["id"]==change:
                print("你要改什么:\033[31mid name age score\033[0m")
                q = input()
                for j in i.keys():
                    if j==q:
                        if j == "name":
                            i[j] = input("改:")
                            m=input("是否还要改 1.改 2.不改 ")
                            if m=="1":
                                a()
                                break
                            elif m=="2":
                                break
                            break
                        else:
                            i[j] = int(input("改吧:"))
                            m = input("是否还要改 1.改 2.不改 ")
                            if m=="1":
                                a()
                                break
                            elif m=="2":
                                break
                            break

                break
    else:
        print("没有该id的学生")
"排序学生"
def sort(j,k):
    if q=="1":
        students.sort(key=lambda x:x[j] )
    elif k=="2":
        students.sort(key=lambda x: x[j],reverse=True)
while True:
    menu()
    res=int(input("请输入对应数字操作："))
    if res==1:
        showstu()
    elif res==2:
        addstu()
    elif res==3:
        delstu()
    elif res==4:
        changestu()
    elif res==5:
        p=input("以什么排序:id age score ")
        q=input("1.正序 2。倒序 ")
        sort(p,q)
    else:
        break




