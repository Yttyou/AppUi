# Author: 田宇恒
# Create Date: 2020/03/16
# Last updated Date: 2020/03/16

import json

# # 获取带有分支提交人的真实姓名的 gitinfo
# def get_git_info_with_real_names():
#     # 提交信息读取
#     git_info = json.load(open('./allure-report/html/data/gitinfo.json', encoding='utf-8'))
#     # 名单读取
#     roster_list = json.load(open('./TestFiles/roster.json', encoding='utf-8'))
#     # 提交人获取
#     commit_account_names = []
#     for commit in git_info:
#         commit_account_names.append(commit.get('name'))
#         # 遍历名单，匹配 account_name
#         for roster in roster_list:
#             if roster.get('account_name') == commit.get('name'):
#                 commit.update({'real_name': roster.get('real_name')})
#                 break
#         # 当无法匹配到真实人名时，BC 推送报告中只可显示 gitinfo.json 中的 name 作为替代
#         else:
#             commit.update({'real_name': commit.get('real_name')})
#     return git_info

# 获取相应分支提交人所对应的 PO
def get_commit_dev(git_name):
    # # 提交信息读取
    # git_info = json.load(open('./allure-report/html/data/gitinfo.json', encoding='utf-8'))
    # # 当 gitinfo.json 中无数据的时候，方法返回`Neptune.AI`
    # if len(git_info) == 0:
    #     return None
    # # 提交人(当 gitinfo.json 中与多条数据的时候，仅获取最后一行记录对应的值)
    # commit_account_name = git_info[len(git_info) - 1].get('name')
    commit_account_name = git_name
    # 名单读取
    roster_list = json.load(open('./TestFiles/roster.json', encoding='utf-8'))
    # 遍历名单，匹配 account_name，获取 PO
    for roster in roster_list:
        if roster.get('account_name') == commit_account_name:
            return roster.get('real_name')
    # 当在 roster.json 中匹配不到数据的时候，方法返回`Neptune.AI`
    else:
        return commit_account_name


# 获取相应分支提交人所对应的 PO
def get_commit_po(git_name):
    # # 提交信息读取
    # git_info = json.load(open('./allure-report/html/data/gitinfo.json', encoding='utf-8'))
    # # 当 gitinfo.json 中无数据的时候，方法返回`Neptune.AI`
    # if len(git_info) == 0:
    #     return 'Neptune.AI'
    # # 提交人(当 gitinfo.json 中与多条数据的时候，仅获取最后一行记录对应的值)
    # commit_account_name = git_info[len(git_info) - 1].get('name')
    commit_account_name = git_name
    # 名单读取
    roster_list = json.load(open('./TestFiles/roster.json', encoding='utf-8'))
    # 遍历名单，匹配 account_name，获取 PO
    for roster in roster_list:
        if roster.get('account_name') == commit_account_name:
            return roster.get('PO')
    # 当在 roster.json 中匹配不到数据的时候，方法返回`Neptune.AI`
    else:
        return 'Neptune.AI'


# 获取相应分支提交人所对应的 PO
def get_commit_po_4_bug():
    # 提交信息读取
    git_info = json.load(open('./TestFiles/gitinfo.json', encoding='utf-8'))
    # 当 gitinfo.json 中无数据的时候，方法返回`Neptune.AI`
    if len(git_info) == 0:
        return 'Neptune.AI'
    # 提交人(当 gitinfo.json 中与多条数据的时候，仅获取最后一行记录对应的值)
    commit_account_name = git_info[len(git_info) - 1].get('name')
    # commit_account_name = git_name
    # 名单读取
    roster_list = json.load(open('./TestFiles/roster.json', encoding='utf-8'))
    # 遍历名单，匹配 account_name，获取 PO
    for roster in roster_list:
        if roster.get('account_name') == commit_account_name:
            return roster.get('PO_ZT')
    # 当在 roster.json 中匹配不到数据的时候，方法返回`Neptune.AI`
    else:
        return 'tlf.yj'
