
"""  该文件为数据记录文件  """

import random
import json
import logging
from Common import logger
from TestDatas.account_data import account_list
from Common.path_config import testdatas_path

"""  获取登录账号方式一：指定账号  """
user = "cfruit.mxn02"
passwd = "Aa123456"

"""  获取登录账号方式二 ：随机抽取一个   """
# def random_account():
#     test_code = random.sample(account_list,1)
#     return test_code[0]

# user = random_account()["user"]
# passwd = random_account()["passwd"]


# ------------- 回归测试，救命清单 IM发送消息功能相关文本   -------------------
IM_chat_send_text1 = "哈哈哈"


# ------------- 【聊天】模块相关用例使用测试数据-------------------
# 讯息页-搜索关键词
message_search_text = "test"

# 讯息页创建群组-群组命名
create_group_name = "test高级群"

# 创建群组-添加联络人数
create_group_user_times = 3

# 個人頁分享自己帖子，文本
share_personal_text = "我自己的帖子自己分享咯"

# 聊天輸入與輸出
chat_data = [{"text": "測試中文", "result": "測試中文"},
             {"text": "test input", "result": "test input"},
             {"text": "789", "result": "789"},
             {"text": "[xxl01](user://66666618)", "result": "xxl01"},
             {"text": "[xxl01]", "result": "[xxl01]"},
             {"text": "[Fist][Pinky][RockOn][Beckon]", "result": "[Fist][Pinky][RockOn][Beckon]"},
             {"text": "https://www.taobao.com/", "result": "https://www.taobao.com/"},
             {"text": "[zu88](crm://4000029818)", "result": "zu88"}]

# keycode 对照表
keycode = {'a':29,'b':30,'c':31,'d':32,'e':33,'f':34,'g':35,'h':36,'i':37,'j':38,'k':39,'l':40,'m':41,
           'n':42,'o':43,'p':44,'q':45,'r':46,'s':47,'t':48,'u':49,'v':50,'w':51,'x':52,'y':53,'z':54,
           '0':7,'1':8,'2':9,'3':10,'4':11,'5':12,'6':13,'7':14,'8':15,'9':16}

# 個人頁面「設定昵稱和標簽」輸入暱稱文本
name_label_data = "這是一個標準暱稱"

# 個人頁面[查找聊天内容]-输入文本信息
find_chat_text = "mirtest"

# ------------- 【最新动态】模块相关用例使用测试数据-------------------
# 最新动态-搜索关键词
search_test = "test"

# 最新动态-搜索用戶关键词
search_user_test = "cfruit"

# [建立群組]名稱文本
create_group_text = "123"

# 發帖內容
post_fend_text = "發帖內容-"

#發帖內容多种组合字符
post_send_texts = "这是一个神奇的帖子@#￥&sdsd-"

# 动态留言-文本
send_message = "来都来了，说点什么吧！+1"

# 個人tab發帖文本
personal_post_text = "個人帖子-"

# 投標標題
vote_title = "來投個票吧-"

# 投票內容
vote_text = "這個字你會念嗎？-"

# 动态留言回复前置，创建一个留言-文本
send_message_data = "我来创建一个留言吧zzz"

# 分享动态文本
share_post_text = "来神秘人的转发！"

# 对评论的回复文本
send_message_reply = "小可爱！！来了也不打声招呼"

# 动态留言-回复文本
reply_message = "别点我，我只是来回复的...+2"

# 分享动态，编辑文本
share_text = "来着神秘的分享"

# 設定暱稱
user_name = "備註名-"

vote_title_str = "这是一个投票标题"
vote_content_str = "这是一个投票内容"