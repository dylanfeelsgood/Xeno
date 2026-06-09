#每个联系人是字典，多个联系人信息集合是列表。 即 列表里面装字典

# contacts = {
#     "name":"xeno",
#     "tel":"123456",
#     "email":"xeno @ qq.com"
# }
#
# print(contacts)


#联系人信息添加
def add_contact(contacts):
    name = input("请输入联系人姓名：")
    tel = input("请输入联系人电话：")
    email = input("请输入联系人邮箱地址：")

    contact = {"name":name,"tel":tel,"email":email}
    contacts.append(contact)
    print(f"已添加联系人:{name}的联络信息")

#联系人信息删除
def delete_contact(contacts):
    if not contacts:
        print("未登记任何联系人信息")
        return
    name = input("请输入要删除的联系人姓名：")
    for contact in contacts:
        if name == contact["name"]:
            contacts.remove(contact)
            print(f"已删除联系人:{name}")
            return
    print(f"未找到该联系人:{name}信息")

#已有联系人信息修改
def update_contact(contacts):
   if not contacts:
       print("未登记任何联系人信息")
       return
   name_search = input("请输入要修改的联系人姓名：")
   found = False
   for contact in contacts:
       if contact["name"] == name_search:
           name_update = input(f"请输入该用户的姓名(按回车跳过){contact['name']}:")
           tel_update = input(f"请输入该用户的电话(按回车跳过){contact['tel']}:")
           email_update = input(f"请输入该用户的邮箱(按回车跳过){contact['email']}:")

           if name_update:
               contact['name'] = name_update
           if tel_update:
               contact['tel'] = tel_update
           if email_update:
               contact['email'] = email_update

           print(f"已成功修改联系人{contact['name']}的信息")
           found = True
           break
   if not found:
       print(f"未找到该联系人:{name_search}信息")

#展示通讯录信息
def display_all_contacts(contacts):
    if not contacts:
        print("未登记任何联系人信息")
        return
    for contact in contacts:
        print(f"姓名: {contact['name']}\t电话: {contact['tel']}\t邮箱: {contact['email']}")
        print("-----------------\n")

#查询联系人
def search_contact(contacts):
    if not contacts:
        print("未登记任何联系人信息")
        return
    name = input("请输入要查找的联系人姓名：")
    found = False
    for contact in contacts:
        if name == contact["name"]:
            print(f"联系人姓名:{contact['name']}\t联系人电话：{contact['tel']}\t联系人邮箱{contact['email']}")
            found = True
    if not found:
        print(f"未找到该联系人:{name}信息")

#主菜单
def main():
    contacts = []
    while True:
        print("""
====== 通讯录系统 ======
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