__author__ = 'developer'

# 【最新动态】页面元素定位
from appium.webdriver.common.mobileby import MobileBy as Mb


class NewdynamicTabLocator:
    # --------------------------- 【全部】相关元素定位  ------------------------------------------------
    appPackage = "com.suncity.sunpeople.qa"

    all_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_tab_all")  # 全部tab
    all_tab_post_entrance = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_all_header_search")        # [你在想什麼?]入口

    message_count = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_message_count")  # 全部tab-留言计数（多个，不唯一）
    all_tab_photo_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_all_header_camera")    # 全部tab-拍照icon
    message_input = (Mb.ID, "com.suncity.sunpeople.qa:id/comment_input_edittext")       # 留言输入框
    message_details_retun_button = (Mb.ID, "com.suncity.sunpeople.qa:id/rl_left")       # 动态详情页【返回】按钮
    send_button = (Mb.ID, "com.suncity.sunpeople.qa:id/comment_input_push_news")        # 留言-发布按钮
    leave_like_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_laud")        # 动态-点赞按钮（多个，不唯一）
    post_page_like_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_laud")       # 帖子详情页-点赞icon


    leave_like_time = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_laud_count")    # 动态计数
    comment_reply = (Mb.ID, "com.suncity.sunpeople.qa:id/comment_first_reply")          # 动态评论中-回复（多个，不唯一）
    dynamic_user_avatar = (Mb.ID, "com.suncity.sunpeople.qa:id/iv_avatar")              # 全部tab中第一个动态用户头像
    one_share_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_share")          # 全部tab中第一個可分享動態分享icon（不唯一）
    list_share_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")  # 分享下拉列表-[分享]
    share_to_SP_button = (Mb.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.TextView\").textContains"
                                                  "(\"分享至SunPeople Chat\").resourceId(\"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title\")")  # 分享下拉列表-[分享至SunPeople]
    share_input = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_share_edit")  # 分享动态页面-分享文本输入框
    share_page_share_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_share_to_group_bt")  # 分享动态页面-分享按钮
    dialog_page_one_user = (Mb.ID, "com.suncity.sunpeople.qa:id/view_forwardmessage_item_givenname")  # 最新对话页-第一个对象
    share_time = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_share_count")  # 分享計數
    share_users = (Mb.ID, "com.suncity.sunpeople.qa:id/ll_item_content")  # 分享帖子頁-用戶（多個）
    vote_title_text = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_content_text")  # 全部tab中发布的投票标题
    post_vote_cutoff_time = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_vote_date")          # 投票的截止时间栏（不唯一）
    post_vote_text = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_vote_title_name")           # 全部tab中发布的投票内容
    post_vote_Option_text = (Mb.ID,"com.suncity.sunpeople.qa:id/item_nf_vote_name")     # 全部tab中发布的投票-選項
    post_like_count_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_laud_count")    # 列表帖子點讚計數icon
    post_detail_like_count_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_laud_count")  # 帖子详情點讚計數icon
    like_page_count = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_like_or_share_txt")        # 「讚好帖子」頁面-點讚數
    post_like_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_laud")            # 帖子點讚icon
    post_comment_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_message")      # 帖子留言icon
    post_share_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_share")          # 帖子分享icon
    post_page_comment_input = (Mb.ID,"com.suncity.sunpeople.qa:id/comment_input_edittext")  # 帖子詳情頁-留言輸入框
    comment_release_button = (Mb.ID,"com.suncity.sunpeople.qa:id/comment_input_push_news")  # 留言發佈按鈕
    post_comment_number_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_message_count") # 帖子詳情頁-留言計數icon
    post_share_number_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_share_count")     # 帖子-分享計數icon
    post_share_to_share = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")       # 分享icon-"分享"
    share_to_done = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_share_to_group_bt")               # 分享icon-"分享"-[分享]確認按鈕
    post_share_to_sp = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_ll")             # 分享icon-"分享至sp"
    post_share_to_sp_user = (Mb.ID,"com.suncity.sunpeople.qa:id/view_forwardmessage_item_givenname")  # "分享至sp"-分享對象列表每項
    publish_dynamic = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_all_header_search")            # '你在想什麼?'發帖入口
    publish_input = (Mb.ID, "com.suncity.sunpeople.qa:id/publish_edit")                     # 「建立貼文」頁面-輸入框
    personal_dynamic = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_publish_group_name")         # "建立体文"页面-[個人動態]跳转按钮
    share_page_list = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_share_group_name")            # "分享至"页面列表
    send_post_cancel = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_publish_close")              # 发帖中-【取消】按钮
    all_tab_post_text = (Mb.ID, 'com.suncity.sunpeople.qa:id/nf_news_item_content_text')     # 全部tab中-帖子文本
    post_page_share_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_share")        # 帖子詳情-分享icon
    all_tab_post_user_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_avatarView")    # 帖子列表用户头像
    user_homepage_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_user_item_user_name")       # 用戶主頁暱稱
    all_tab_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_user_name")        # 帖子列表用户昵称
    photo_download = (Mb.ID,"com.suncity.sunpeople.qa:id/act_imagepreview_download")        # 图片详情下载按钮

    # --------------------------- 【群组】相关元素定位  ------------------------------------------------
    loading_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/blv_pb")                             # loading提示
    qroup_loading_icon = (Mb.ID,'com.suncity.sunpeople.qa:id/nf_loading_img')               # 進入群组load

    group_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_tab_user_group_img")                # 群组tab
    create_group_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_create")             # [建立群組]按鈕
    explore_group_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_search_bt")         # [探索群組]按鈕
    track_more_track_button = (Mb.ID,'com.suncity.sunpeople.qa:id/followBtn')               # "追蹤更多"頁面群組tab-「追蹤」按鈕（不唯一）
    quit_group_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_dialog_right_bt")            # 退出群组弹框-【確定退出】按钮
    track_more_group_list = (Mb.ID,'com.suncity.sunpeople.qa:id/followGroupName')           # "追蹤更多"頁面群組tab-群組名稱（不唯一）
    track_more_navigate = (Mb.ID,'com.suncity.sunpeople.qa:id/nf_trace_more_sidebar')       # "追蹤更多"頁面群組tab-[導航欄]
    track_more_personal_track_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_fans_following")  # "追蹤更多"頁面個人tab-「追蹤」按鈕（不唯一）
    track_more_personal_list = (Mb.ID, 'com.suncity.sunpeople.qa:id/nfNameTitle')           # "追蹤更多"頁面個人tab-用戶名稱（不唯一）
    list_head_title = (Mb.ID,'com.suncity.sunpeople.qa:id/item_head_title')                 # 群組列表中群組首字母
    create_group_name_input = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_edit_name")      # 群組名稱輸入框
    create_group_done_button = (Mb.ID,'com.suncity.sunpeople.qa:id/nf_create_group_bt')     # [建立群組]完成按鈕
    track_more_search_box = (Mb.ID,"com.suncity.sunpeople.qa:id/et_search")                 # "追蹤更多"頁面-[搜索]框
    track_more_search_grouplist = (Mb.ID,"com.suncity.sunpeople.qa:id/followGroupName")     # 群組搜索結果文本（不唯一）
    group_post_list_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_user_name")    # 群組tab列表中帖子用戶暱稱
    track_more_personal_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/rbPersonal")              # "追蹤更多"頁面-[個人]tab
    track_page_personal_track_button = (Mb.ID,'com.suncity.sunpeople.qa:id/nf_fans_following')      # "追蹤更多"頁面個人tab-[追蹤]按鈕
    list_one_track_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nfNameTitle")                  # 個人tab中第一個"追蹤"的用戶名稱
    list_track_group_name = (Mb.ID,'com.suncity.sunpeople.qa:id/tvName')                     # 個人tab中追蹤中群組名稱（不唯一）
    list_track_group_title = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_trace_header_num")       # 個人tab中追蹤中-'n個群組追蹤中'
    group_page_group_title = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_item_group_name")  # 群組主頁-獲取群組名稱
    group_tab_view_all = (Mb.ID,"com.suncity.sunpeople.qa:id/tvTraceMore")                   # 群組tab-「查看全部」icon
    your_group_list = (Mb.ID,"com.suncity.sunpeople.qa:id/followGroupName")                  # "你的群組"頁面列表中群組（不唯一）
    group_home_group_count = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_item_group_info")  # 群組主頁-統計成員個數欄
    group_home_member_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/avatar")               # 群組主頁-成員頭像
    fend_page_admin_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/groupMember_tabView_text")     # "成员和粉丝"页面-【x位管理员】tab（不唯一）
    group_member_list = (Mb.ID,"com.suncity.sunpeople.qa:id/news_feed_member_content_layout")   # "成員和粉絲"頁面沒列（不唯一）
    your_group_admin = (Mb.ID,"com.suncity.sunpeople.qa:id/item_header_text")                # "你的群组"页面-"群組管理員"栏
    your_group_following_tab = (Mb.CLASS_NAME,"androidx.appcompat.app.ActionBar$Tab")        # "你的群组"页面-【追踪中】tab(不唯一)
    your_group_page_other_tab = (Mb.ACCESSIBILITY_ID,"其他")                                  # "你的群组"页面-【其他】tab
    your_group_following_tab_list = (Mb.ID,"com.suncity.sunpeople.qa:id/followGroupName")    # "你的群组"页面-【追踪中】tab中每列
    following_tab_list_following_button = (Mb.ID,"com.suncity.sunpeople.qa:id/followBtn")    # "你的群组"页面-【追踪中】tab中「追蹤中」按鈕
    other_tab_user_list = (Mb.ID,"com.suncity.sunpeople.qa:id/followGroupName")              # "你的群组"页面-【其他】tab - 用户昵称每列
    other_tab_track_button = (Mb.ID,"com.suncity.sunpeople.qa:id/followBtn")                 # "你的群组"页面-【其他】tab - [追踪]按钮
    group_page_one_post_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_user_name")    # 群組tab帖子用戶暱稱（不唯一）
    group_page_one_post_user_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_avatarView")          # 群組tab帖子用戶頭像（不唯一）
    personal_page_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_user_item_user_name")     # 個人主頁用戶暱稱欄
    group_home_page_quit_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_item_track")    # 群組主頁群[退出]按鈕
    group_tab_one_post_text = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_content_text")  # 群组tab中第一个贴子的文本
    set_post_admin_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_publish_admin_type_bt")     # 建立贴文页面-【管理员身份】下拉按钮
    public_post_buttn = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_publish_group_private")         # 建立贴文页面- [公開帖文]下拉列表
    group_tab_post_like_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_laud")         # 列表中帖子點讚icon
    group_tab_post_like_count = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_laud_count")  # 列表中帖子點讚計數欄
    group_tab_post_leave_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_message")     # 列表帖子留言icon
    group_tab_post_share_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_share")       # 列表帖子分享icon
    group_tab_post_share_Option = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")  # 列表帖子分享-分享
    group_tab_post_share_Option_to_done = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_share_to_group_bt")    # 列表帖子分享-分享-分享
    create_group_avatar_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_add_cover")         # '建立群組'頁面-「新增封面相片」
    avatar_photo_icon = (Mb.CLASS_NAME,"android.widget.ImageView")                              # 「新增封面相片」-[相冊]
    avatar_photo_always = (Mb.ID,"android:id/button_always")                                    # [相冊]-[始终]
    avatar_photo_list = (Mb.ID,"com.sec.android.gallery3d:id/thumbnail")                        # [相冊]頁面-圖片框（不唯一）
    avater_photo_button = (Mb.ID,"com.sec.android.gallery3d:id/title")                          # [相冊]頁面-[图片]按钮
    create_group_private_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_rb_private")             # '建立群組'頁面-[私密]單選按鈕
    create_group_add_member_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_choose_user")         # '建立群組'頁面-[新增成員]
    add_member_list = (Mb.ID,"com.suncity.sunpeople.qa:id/ll_item_content")                     # '新增成員'頁面-人員列表（不唯一）
    add_member_done_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")               # '新增成員'頁面-[完成]按鈕

    your_all_groups = (Mb.ID, "com.suncity.sunpeople.qa:id/tvTraceMore")                        # 查看全部群組
    your_group_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_group_rc_view")                 # 你的群組
    your_group_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_group_tabLayout")                  # 你的群組頂部導航欄
    your_group_page_list = (Mb.ID, "com.suncity.sunpeople.qa:id/ll_item_content")               # 你的群組成員-列表
    share_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_share")                      # 动态分享icon
    share_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")                # 分享列表中-分享
    share_to = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")                    # 分享列表中-分享至SunPeople Chat

    group_dynamic_list_detail = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_user_name")  # 群組詳情
    group_dynamic_list_detail_group_name = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_group_item_group_name")  # 群組詳情-群組名稱
    group_dynamic_list_detail_user_name = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_user_name")  # 群組詳情-成員名稱

    your_group_tab_item_members = (Mb.ACCESSIBILITY_ID, "成員")
    your_group_tab_item_trance = (Mb.ACCESSIBILITY_ID, "追蹤中")
    your_group_tab_item_others = (Mb.ACCESSIBILITY_ID, "其他")

    # --------------------------- 【通知】相关元素定位  ------------------------------------------------
    notice_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_tab_news_notify_img")               # 通知tab
    notice_list_message = (Mb.ID,"com.suncity.sunpeople.qa:id/news_message_content")        # 通知tab中列表中数据
    chat_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/rl_chat")                               # 底部导航栏【聊天】

    # --------------------------- 【个人】相关元素定位  ------------------------------------------------
    personal_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_tab_user_bt")                    # 【个人】tab
    trace_group_Avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_icon")                # "追踪中"tab-追踪的群组头像
    nf_load_img = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_loading_img")                      # 數據加載icon
    personal_tab_photo_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_all_header_camera")    # [个人]【全部】tab-拍照icon
    personal_pro = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_user_blvLoading")                # 【个人】网络进度条消失
    personal_tab_fan = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_user_item_fans_count")       # 【個人】tab-粉丝计数
    fan_list_count = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_fans_header_num")               # 【個人】tab-粉丝计数-詳情頁-統計數
    personal_trace = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_user_item_track_to")           # 【個人】追蹤中
    personal_trace_number = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_fans_header_num")        # 追蹤中tab-个人追踪统计数
    personal_trace_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nfNameTitle")            # 追蹤中-列表用戶暱稱
    personal_tab_shart_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_share")     # 個人tab-第一个可分享动态分享icon
    trace_too_list = (Mb.ID,'com.suncity.sunpeople.qa:id/nfNameTitle')                      # 個人tab-追踪中tab 列表沒行（不唯一）
    personal_home_page_trace = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_user_item_track")     # 用戶主頁[追踪中]按鈕
    personal_home_page_trace_fix = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_dialog_right_bt") # 用戶主頁[追踪中]-[確認取消]按鈕
    personal_home_trace_group = (Mb.ID,'com.suncity.sunpeople.qa:id/nf_group_operation')    # 用戶主頁追踪中的群组主页-更多icon
    trace_group_cancel_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")  # 更多icon- [取消追蹤]按鈕
    personal_post_entrance_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_all_header_search")  # [在想些什麼?]发帖入口
    post_inptu_box = (Mb.ID,"com.suncity.sunpeople.qa:id/publish_edit")                     # '請輸入想要分享的內容'文本輸入框
    post_publish_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")              # [發佈]按鈕
    release_post_time = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_user_title_date")  # 發佈帖子的時間展示欄（不唯一）
    personal_tab_post_text = (Mb.ID,'com.suncity.sunpeople.qa:id/nf_news_item_content_text')    # 帖子文本（不唯一）
    add_more_element_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/publish_bottom_head")       # 【添加更多元素】icon
    vote_page_set_post = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"建立帖文\")."
                    "resourceId(\"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title\")")       # 提交投票页面-添加更多元素-建立帖文
    submit_vote = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")              # [提交投票]选项
    submit_vote_add_Option = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_publish_add_vote")      # [提交投票]-[添加選項]按鈕
    add_Option3 = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.EditText\").textContains(\"選項3\")")  # 選項3
    add_Option4 = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.EditText\").textContains(\"選項4\")")  # 選項3
    input_vote = (Mb.CLASS_NAME,"android.widget.EditText")                                  # [提交投票]选项 選項輸入框（不唯一）
    share_group = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_publish_group_name")               # [群組]分享下拉列表
    share_list_number = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_share_group_name")           # [分享至]页-列表每列群組（不唯一）
    share_done_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")                # [分享至]页-[完成]按钮
    publish_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")                   # 建立貼文頁面-「發帖」按鈕
    multiple_choice_off = (Mb.ID,"com.suncity.sunpeople.qa:id/view_loadingswitch_sc")       # 提交投票-「可多選」開關icon
    vote_end_time = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_publish_vote_select_time")       # 提交投票-[投票結束時間]選項
    list_time_days = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")           # [投票結束時間]選項-时间选项（不唯一）
    post_publish_cancel = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_publish_close")            # 帖子发布中-【取消】按钮
    personal_post_share_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_share")     # 個人tab中帖子分享icon
    share_nf_Jump_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_share_to_group_cl")         # '分享動態'頁面-分享至跳轉icon
    share_nf_group_list = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_frame_share_group")        # '分享至'页面群组列表每项（不唯一）
    share_nf_group_done = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")              # '分享至'页面-[完成]按钮
    share_nf_input = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_share_edit")                    # '分享動態'頁面-输入框
    callout_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")             # 【标注人名】选项
    callout_name_page_list_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nfDisPlayName")       # '标注人名'頁面-列表用戶暱稱（不唯一）
    callout_name_page_done = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")           # '标注人名'頁面-[完成]按鈕
    callout_name_page_search = (Mb.ID,"com.suncity.sunpeople.qa:id/et_search")              # '标注人名'頁面-[搜索]框
    post_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_user_name")           # 帖子展示的用戶名欄(不唯一)
    photo_Check_button = (Mb.ID,"com.suncity.sunpeople.qa:id/v_photoView_tvNum")            # 相片複選按鈕
    photo_send_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_send")                       # 選擇照片頁-「傳送」按鈕
    photo_delete_button = (Mb.CLASS_NAME,"android.widget.Button")                           # 照片刪除按鈕
    set_post_page_return = (Mb.ID,'com.suncity.sunpeople.qa:id/tv_left_title')              # "建立贴文"页面-【返回】按钮
    return_quit_draft = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title")        # [放棄發佈]按鈕
    photo_page_cancel_button = (Mb.ID,"com.suncity.sunpeople.qa:id/photo_cancel")           # 選擇照片頁面-「取消」按鈕
    personal_tab_shutter_button = (Mb.ID,"com.suncity.sunpeople.qa:id/cameraButtonView")    # 快門icon
    personal_tab_media_cancel = (Mb.ID,"com.suncity.sunpeople.qa:id/media_cancel")          # [重做]按鈕
    personal_tab_send_button = (Mb.ID,"com.suncity.sunpeople.qa:id/media_send")             # 拍照頁面-「傳送」按鈕
    save_draft_button = (Mb.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.TextView\").'
        'textContains(\"存為草稿\").resourceId(\"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title\")')     # [存為草稿]按鈕
    abandon_post_button = (Mb.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.TextView\").'
        'textContains(\"放棄發布\").resourceId(\"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title\")')      # [放棄發佈]按鈕
    trace_more_personal_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/rbPersonal")              # '追蹤更多'頁面-「個人」tab

    personal_tab_post_more_button = (Mb.ID,"com.suncity.sunpeople.qa:id/item_edit_bt")      # 个人tab-帖子更多icon
    more_list_delete_button = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\")."
                     "textContains(\"刪除帖子\").resourceId(\"com.suncity.sunpeople.qa:id/nf_bottom_dialog_title\")")  # 帖子更多icon-[删除]帖子
    more_list_delete_button_confirm = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_dialog_right_bt")  # [删除]帖子-[確認刪除]按钮
    all_tab_post_photo = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_img_one")        # 帖子中图片定位（不唯一）
    all_tab_post_video = (Mb.ID,"com.suncity.sunpeople.qa:id/thumb")                       # 帖子中视频定位（不唯一）
    post_video_play_progress = (Mb.ID,"com.suncity.sunpeople.qa:id/progress")                   # 视频播放进度条

    # --------------------------- 【个人】粉丝  ------------------------------------------------
    personal_fans_item = (Mb.ID, "com.suncity.sunpeople.qa:id/ll_item_content")
    personal_fans_loading_view = (Mb.ID, "com.suncity.sunpeople.qa:id/nfLoadingView")

    # --------------------------- 【个人】追踪  ------------------------------------------------
    personal_trace_item = (Mb.ID, "com.suncity.sunpeople.qa:id/ll_item_content")                    # 个人追踪 item
    personal_trace_item_nickname = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_fans_name")              # 个人追踪 nickname
    personal_trace_item_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_fans_following")           # 个人追踪 button
    personal_trace_item_button_commit = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_dialog_right_bt")   # 个人追踪 button 弹窗 确定取消

    # --------------------------- 【搜索】相关元素定位  ------------------------------------------------
    Newdynamic_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_notifi")  # 导航栏-【最新动态】

    search_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_tab_search_tv")  # 【最新动态】tab-【搜索】按钮

    search_input = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_search_search")  # 搜索输入栏

    # [搜索]功能页元素定位
    poat_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_search_post")                      # 【贴文】按钮
    view_user_all_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_search_user_all")         # 用户【查找全部】
    view_post_all_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_search_post_all")         # 贴文【查找全部】
    group_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_search_group")                    # 【群组】按钮
    public_group_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_group_public_name")        # 群组--【公共群组】按钮
    public_group_icon = (Mb.ID,'com.suncity.sunpeople.qa:id/item_head_name')                 # 群组-【公共群组】icon
    user_button = (Mb.ANDROID_UIAUTOMATOR,
                   "new UiSelector().className(\"android.widget.TextView\").textContains(\"用戶\").resourceId(\"com.suncity.sunpeople.qa:id/nf_search_user\")")  # 【用户】按钮
    # 用户--【追踪】按钮
    track_button = (Mb.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className(\"android.widget.TextView\").textContains(\"追蹤中\").resourceId(\"com.suncity.sunpeople.qa:id/nf_fans_following\")')
    search_group_track_button = (Mb.ID,"com.suncity.sunpeople.qa:id/followBtn")             # 搜索'群組'列表中-「追蹤」按鈕
    search_group_name_list = (Mb.ID,"com.suncity.sunpeople.qa:id/followGroupName")          # 搜索'群組'列表中-群組名稱
    search_user_track_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_fans_following")      # 搜索'用戶'列表中-「追蹤」按鈕
    search_user_name_list = (Mb.ID,"com.suncity.sunpeople.qa:id/nfNameTitle")               # 搜索'用戶'列表中-用戶名稱
    user_home_track_to_button = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_user_item_track")    # 用戶主頁-「追蹤中」按鈕
    user_home_track_cancel = (Mb.ID,"")
    cancel_button = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_search_cancel")                 # 搜索页-【取消】按钮
    cancel_track_prompt = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_dialog_left_bt")           # "取消追踪"弹框-【取消】按钮

    personal_fans_first_username = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_fans_name")
    personal_fans_first_text = (Mb.ID, "com.suncity.sunpeople.qa:id/et_search")
    list_one_search_name= (Mb.ID,"com.suncity.sunpeople.qa:id/ll_item_content")              # 搜索显示的粉丝名称
    first_message_count= (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_message_count")    # 搜索粉丝名称点击跳转显示的第一个留言个数
    first_message_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_message")          # 搜索粉丝名称点击跳转显示的第一个留言icon
    first_share_count = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_news_item_share_count")      # 搜索粉丝名称点击跳转显示的第一个分享个数
    first_share_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_news_item_share")              # 搜索粉丝名称点击跳转显示的第一个分享icon
    submit_to_vote = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_bottom_dialog_bt")                 # 提交投票
    vote_title = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_publish_vote_title")                   # 投票标题
    vote_content = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_publish_vote_context")               # 投票内容
    choose_day = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_bottom_dialog_bt")                      # 天数选择
    choose_group = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_publish_group_name")                 # 群组选择
    share_to_group = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_frame_share_group")                # 分享至群组选择
    click_finish = (Mb.ID, "com.suncity.sunpeople.qa:id/rl_right")                              # 点击完成
    one_select = (Mb.ID, "com.suncity.sunpeople.qa:id/item_nf_vote_select")                     # 投票单选
    push_vote = (Mb.ID, "com.suncity.sunpeople.qa:id/nf_vote_publish_bt")                       # 提交投票
    more_select = (Mb.ID, "com.suncity.sunpeople.qa:id/view_loadingswitch_sc")
    the_invitation = (Mb.ID,"com.suncity.sunpeople.qa:id/nf_group_operation")                   # 邀请
    search_one_member = (Mb.ID,"com.suncity.sunpeople.qa:id/ll_item_content")                   # 搜索出来的第一个成员
    home_app_name = (Mb.ID,'new UiSelector().className(\"android.widget.TextView\").textContains(\"SunPeopleQA\").'
                           'resourceId(\"com.sec.android.app.launcher:id/iconview_titleView\")')    # 手机主页app图标下的名字
    app_Subscript  = (Mb.ID,"com.sec.android.app.launcher:id/iconview_badge")                       # app角标
