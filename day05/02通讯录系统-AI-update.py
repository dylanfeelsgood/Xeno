import json

FILE_NAME = "contacts.json"

#读取记忆
def load_contacts():
    try:
        with open(FILE_NAME,"r",encoding="utf-8") as file:
            contacts = json.load(file)
            return contacts
    except:
        return []

#保持记忆
def save_contacts(contacts):
    with open(FILE_NAME,"w",encoding="utf-8") as file:
        json.dump(contacts,file,ensure_ascii=False,indent=2)

#联系人信息添加
def add_contact(contacts):
    name = input("请输入联系人姓名：")
    tel = input("请输入联系人电话：")
    email = input("请输入联系人邮箱地址：")

#去重
    for c in contacts:
     if c["name"] == name or c["tel"] == tel or c["email"] == email:
        print("已存在相同联系人")
        return
    contacts.append({"name":name,"tel":tel,"email":email})
    save_contacts(contacts)
    print(f"已添加联系人:{name}的联络信息")

#联系人信息删除
def delete_contact(contacts):
    if not contacts:
        print("未登记任何联系人信息")
        return

    name = input("请输入要删除的联系人姓名：")
    for c in contacts:
        if c["name"] == name:
            contacts.remove(c)
            save_contacts(contacts)
            print(f"已删除联系人")
            return

    print(f"未找到该联系人信息")

#已有联系人信息修改
def update_contact(contacts):
   if not contacts:
       print("未登记任何联系人信息")
       return
   name_search = input("请输入要修改的联系人姓名：")
   found = False
   for c in contacts:
       if c["name"] == name_search:
           name_update = input(f"请输入该用户的姓名(按回车跳过){c['name']}:")
           tel_update = input(f"请输入该用户的电话(按回车跳过){c['tel']}:")
           email_update = input(f"请输入该用户的邮箱(按回车跳过){c['email']}:")

           if name_update:
               c['name'] = name_update
           if tel_update:
               c['tel'] = tel_update
           if email_update:
               c['email'] = email_update
           save_contacts(contacts)
           print(f"已成功修改联系人{c['name']}的信息")
           found = True
           break
   if not found:
       print(f"未找到该联系人信息")

#展示通讯录信息
def display_all_contacts(contacts):
    if not contacts:
        print("未登记任何联系人信息")
        return
    for c in contacts:
        print(f"姓名: {c['name']}\t电话: {c['tel']}\t邮箱: {c['email']}")
        print("-----------------\n")

#查询联系人
def search_contact(contacts):
    keyword = input("请输入查询关键词(姓名/电话/邮箱):")
    result = []

    for c in contacts:
        if keyword in c["name"] or keyword in c["tel"] or keyword in c["email"]:
            result.append(c)

    if not result:
        print(f"未找到该联系人信息")
        return

    for c in result:
        print(f"姓名:{c['name']}\t电话:{c['tel']}\t邮箱:{c['email']}")

#主菜单
def main():
    contacts = load_contacts()#修改为带记忆存储的
    while True:
        print("""
====== AI通讯录系统 ======
1. 添加联系人
2. 删除联系人
3. 修改联系人
4. 查询联系人
5. 展示所有联系人
6. 退出
=========================
""")
        choice = input("请选择操作(1-6): ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            display_all_contacts(contacts)
        elif choice == "6":
            print("👋 已退出系统")
            break
        else:
            print("❌ 输入无效，请输入1~6")

# =========================
# 启动程序
# =========================
if __name__ == "__main__":
    main()