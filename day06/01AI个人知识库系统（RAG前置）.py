import json

FILE_NAME = "knowledge.json"

#读取知识库
def load_docs():
    try:
      with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        seen = set()
        unique = []
        for doc in data:
            if doc["title"] not in seen:
                seen.add(doc["title"])
                unique.append(doc)
        return unique
    except FileNotFoundError:
        #明确指定：只有当文件不存在时，才返回空列表
      return []

#保存知识库：让函数接收要保存的数据对象 data
def save_docs(data):
      with open(FILE_NAME, "w", encoding="utf-8") as f:
          #把传入的 data 写入文件
          json.dump(data,f,ensure_ascii=False,indent=2)

#添加文档
def add_docs(data):
    title = input("请输入文档标题：")
    content = input("请输入文档内容：")

    #去重
    for doc in data:
        if doc["title"] == title:
            print("已存在相同标题")
            return

    data.append({"title":title,"content":content})
    print("文档添加成功！")

#删除文档
def del_docs(data):
    if not data:
        print("知识库内容为空")
        return

    title = input("请输入要删除的文档标题：")

    for doc in data:
        if doc["title"] == title:
            data.remove(doc)
            print("删除成功")
            return

    print("未找到该文档")

#展示文档
def display_docs(data):
    if not data:
        print("知识库内容为空")
        return

    for doc in data:
        print(f"""
标题: {doc["title"]}
内容: {doc["content"]}
----------------------""")

# #搜索 版本1
# def search_docs(data,query):
#     result = []
#
#     for doc in data:
#         if query in doc["title"] or query in doc["content"]:
#             result.append(doc)
#
#     return result

#搜索 版本2
def search_docs(data,query):
    results = []

    for doc in data:
        score = 0
        if query in doc["title"]:
            score += 2
        if query in doc["content"]:
            score += 1
        if score > 0:
            results.append((score,doc))
#按相关性排序
    results.sort(key=lambda x:x[0],reverse=True)
    final_results = []
    for item in results:
        final_results.append(item[1])

    return final_results

#回答
def ask_question(data,query):
    results = search_docs(data,query)

    if not results:
        return "没有找到相关内容"

    answer = f"根据{query}的回答如下：\n\n"

    for i,doc in enumerate(results,1):
        answer += f"{i}. {doc["title"]}\n"
        answer += f"     {doc["content"]}\n\n"

    answer += " 数据来源：知识库"
    return answer

# #测试
# docs = load_docs()
#
# # add_docs(docs)
# #
# # del_docs(docs)
# #
# # display_docs(docs)
# #
# # # 测试搜索功能
# # keyword = input("请输入你想搜索的关键词：")
# # search_results = search_docs(docs, keyword)
# #
# # print("\n搜索结果如下：")
# # #打印搜索结果
# # display_docs(search_results)
# print(ask_question(docs, "Python"))
# save_docs(docs)

#主菜单
def main():
    data_contacts = load_docs()
    while True:
        print("""
====== 知识库系统 ======
1. 添加
2. 删除
3. 查询
4. 展示
5. AI
6. 退出
=========================
""")
        choice = input("请选择操作(1-6): ")
        if choice == "1":
            add_docs(data_contacts)
        elif choice == "2":
            del_docs(data_contacts)
        elif choice == "3":
            query = input("请输入关键字：")
            results = search_docs(data_contacts,query)
            if not results:
                print("没找到")
            else:
                for d in results:
                    print(d["title"], ":", d["content"])
        elif choice == "4":
            display_docs(data_contacts)
        elif choice == "5":
            query = input("请输入问题：")
            print(ask_question(data_contacts,query))
        elif choice == "6":
            print("已退出系统")
            break
        else:
            print("输入无效，请输入1~6")

# =========================
# 启动程序
# =========================
if __name__ == "__main__":
    main()