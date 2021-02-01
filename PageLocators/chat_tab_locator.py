__author__ = 'developer'
#导航栏-【聊天】页面元素定位

from appium.webdriver.common.mobileby import MobileBy as Mb

class ChatTabLocator:
    chat_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/rl_chat")  #底部导航栏【聊天】


#--------------【讯息】tab页面-----------------------------

    #搜索模块用例主要使用到的元素定位
    message_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_newchat_tv_message")  #【讯息】tab
    message_search_input = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_search")   #讯息页-搜索栏
    search_details_input = (Mb.ID,"com.suncity.sunpeople.qa:id/et_search")   #搜索详情页-搜索栏
    independent_message_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_indepenInfo")   #搜索详情页-【独立讯息】tab
    message_tab_one = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_result_content")       #搜索详情页-【独立讯息】tab中第一行讯息文本（多个，不唯一）
    drop_down_list_button = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_next")          #讯息中下拉列表按钮（多个，不唯一）
    #user_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_avatar")          #聊天窗口中用户头像
    user_avatar = (Mb.ID, "com.suncity.sunpeople.qa:id/avatarView")  # 聊天窗口中用户头像(@jinwei)
    group_category_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_groupClass")           #搜索详情页-【群组类别】tab
    group_search_results = (Mb.ID,"com.suncity.sunpeople.qa:id/rl_search_result")       #搜索详情页-【群组类别】搜索结果（不唯一）
    group_tab_one = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_next")                   #搜索详情页-【群组类别】列表中第一个下拉按钮（多个，不唯一）
    #group_tab_title = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"聊天記錄\").resourceId(\"com.suncity.sunpeople.qa:id/tv_title\")")        #群组类别列表页-title
    group_tab_title = (Mb.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.TextView").textContains("聊天記錄").resourceId("com.suncity.sunpeople.qa:id/tv_title")')
    group_tab_one_list_one = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_result_content")   #群组类别-聊天记录：记录列表第一列文本内容
    pus_button = (Mb.ID,"android:id/button1")                         #群组类别-通讯录：弹框提示-【取消】按钮
    chatroom_title = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_center_title")     #群组类别-聊天室title
    center_title = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_center_title")       #群组类别-通讯录-聊天窗口title

    #新建对话-主要使用的元素定位
    create_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_create")                               #讯息tab-加号创建icon
    create_new_message_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_create_new_message")     #创建-下拉列表：【新增对话】
    create_channel_button =(Mb.ID,"com.suncity.sunpeople.qa:id/tv_create_channel")              #创建-下拉列表：【新增群组】
    create_indexsidebar = (Mb.ID,"com.suncity.sunpeople.qa:id/indexSidebar")                            #新增對話-字母快速导航栏
    create_new_message_letter_navig = (Mb.ID,"com.suncity.sunpeople.qa:id/view_channelmembers_item_tv_title")       #新增對話-联系人首字母
    create_message_one_low_text = (Mb.ID,"com.suncity.sunpeople.qa:id/view_channelmembers_item_tv_givenname")    #新增对话页-第一行用户名文本定位（多个，不唯一）
    create_group_one_low_text = (Mb.ID,"com.suncity.sunpeople.qa:id/view_createchannelchoose_item_tv_displayname")      #新增群組-第一行用户名文本定位（多个，不唯一）
    personal_chat_title = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_center_title")                 #个页聊天窗口title-用户名
    offline_user = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_avatar")                                    #新增对话页-未上线用户（头像为灰色）
    online_user = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_avatar")                                    #新增对话页-上线用户（有头像）
    tip_box_dial = (Mb.ID,"android:id/button2")                                              #用户登录提示弹框-拨打
    tip_box_cancel = (Mb.ID,"android:id/button1")                                               #用户登录提示弹框-取消
    dial_list_cancel_button = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"取消\")")   #拨打-取消按钮
    default_count_item = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannel_count")               #新增群组页输入框，显示字数个数
    default_count_input = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannel_name")                #新增群组页输入框
    default_count_admin_switch = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannel_admin")          #[設有群組管理員]開關--屬性值：checked
    default_count_leave_group = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannel_autoLeave")       #[允許成員自動退出群組]
    media_cancel_button = (Mb.ID,"com.suncity.sunpeople.qa:id/media_cancel")                            # 拍照時-「重做」按鈕

    # 群組資訊
    chat_droup_admin_switchv = (Mb.ID,"com.suncity.sunpeople.qa:id/view_loadingswitch_sc")              #[設有群組管理員]、[允許成員自動退出群組] 开关 （不唯一）

    #新增对话-新增相片
    next_step_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")                #【下一步】按钮

    add_photo = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannel_avatarTitle")       #新增群组页-【新增相片】icon(未上传前)
    add_to_photo = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannel_avatar")         #新增群组页-【新增相片】icon(上传后)
    touch_outside = (Mb.ID,"com.suncity.sunpeople.qa:id/touch_outside")                   #【新增相片】列表以外部分
    take_photo_button = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"拍照\")")   #列表中-【拍照】
    none_button = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"GLButton\").textContains(\"快门\").resourceId(\"NONE\")")     #拍照-快门按钮 s9
    none_button_s10 = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"GLButton\").textContains(\"拍照\").resourceId(\"NONE\")")     #拍照-快门按钮 s10
    none_button_all = (Mb.ANDROID_UIAUTOMATOR,
                       "new UiSelector().className(\"GLButton\").textMatches(\"拍照|快门\").resourceId(\"NONE\")")  # 拍照-按钮 通用
    take_photo_confirm = (Mb.ID,"com.sec.android.app.camera:id/okay")                   #拍照-【确定】按钮
    take_photo_retry = (Mb.ID,"com.sec.android.app.camera:id/retry")                    #拍照-【重试】按钮
    cutting_done = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"完成\")")   #拍照-剪切页-【完成】按钮
    choose_photo_button = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"選擇照片\")")   #列表中-【选择照片】
    delete_photo_button = (Mb.ANDROID_UIAUTOMATOR,'new UiSelector().className(\"android.widget.TextView\").textContains(\"刪除圖片\")')   #列表中-【删除图片】
    list_cancel_button = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"取消\")")    #列表中-【取消】按钮
    add_people_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannelmembers_tv_search")        #新增成员页面-加号icon
    check_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/view_createchannelchoose_item_iv_select")        #联络人页面-复选icon
    check_done = (Mb.ID,"com.suncity.sunpeople.qa:id/act_createchannelchoos_tv_done")                 #联络人页面-【完成】按钮
    create_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")                                #新增成员页-【建立】按钮



    #讯息列表中左滑-选项
    left_read_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/menu_read")                   #左滑选项-【标记未读】
    left_mute_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/menu_mute")                   #左滑选项-【静音】
    left_archive_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/menu_archive")               #左滑选项-【存档】
    #mute_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_mute")                           # 列表中[静音]图标
    mute_icon = (Mb.XPATH,'//*[@resource-id="com.suncity.sunpeople.qa:id/recyclerView"]/android.view.ViewGroup[1]//*[@resource-id="com.suncity.sunpeople.qa:id/iv_mute"]') # 列表中第一位用戶 [静音]图标@jinwei
    msg_count_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_msg_count")              #列表中[未讀]图标
    list_one_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_item_given_name")        #讯息列表中第一行数据的用户昵称/或群名
    dialogue_list_one_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_item_given_name")       #封存对话页-第一个用户或群组昵称
    archive_drop_down = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_archived")               #讯息页-封存聊天记录下拉

    #聊天窗口
    text_input = (Mb.ID,"com.suncity.sunpeople.qa:id/msgTextView")                      #聊天界面文本輸入框
    sendView_button = (Mb.ID,"com.suncity.sunpeople.qa:id/sendView")                    #【傳送】按鈕
    new_message = (Mb.ID,"com.suncity.sunpeople.qa:id/im_normalitem_text_tv")            #聊天窗口最新消息
    imagebutton_icon = (Mb.CLASS_NAME,"android.widget.ImageButton")                      #聊天窗口下方-语音、表情、图片、拍照、@
    voice_news_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/playView")                     #聊天中语音消息播放icon
    keep_talking_button = (Mb.ID,"com.suncity.sunpeople.qa:id/voiceButtonView")        #【按住说话】按钮
    chat_new_voice_time = (Mb.ID,"com.suncity.sunpeople.qa:id/voiceDurationView")      #生成語音計時（不唯一）
    chat_shutter_button = (Mb.ID,"com.suncity.sunpeople.qa:id/cameraButtonView")       #聊天中-拍摄-快门
    chat_shoot_send_button = (Mb.ID,"com.suncity.sunpeople.qa:id/media_send")           #长按快门-【传送按钮】
    chat_news_video = (Mb.CLASS_NAME,"android.widget.ImageView")                                #聊天窗口中视频消息-播放icon（不唯一）
    chat_select_photo_tick = (Mb.ID,"com.suncity.sunpeople.qa:id/graph_item_tv_num")    #點擊圖片icon-全部頁勾選按鈕（不唯一）
    chat_image_done = (Mb.ID,"com.suncity.sunpeople.qa:id/photo_tv_done")               #選擇圖片頁-【完成】
    chat_news_time = (Mb.ID,"com.suncity.sunpeople.qa:id/timeView")                     #聊天頁最新消息時間（不唯一）
    chat_recording_back_button = (Mb.ID,"com.suncity.sunpeople.qa:id/act_session_jumpBottom")   #聊天窗口中-快速回到底部icon
    droup_chat_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_right_image")                #群聊天中-右上角頭像icon
    group_chat_ar_list = (Mb.ID,"com.suncity.sunpeople.qa:id/name")                         #@列表中用户昵称（不唯一）
    group_chat_message = (Mb.ID,"com.suncity.sunpeople.qa:id/im_normalitem_text_tv")        #聊天窗口中消息文本
    group_chat_authority = (Mb.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("允许")')  #點擊語音時出現的允許彈窗
    chat_img = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_image")                               # 聊天模块中图片、视频icon
    chat_img_enlarge_download = (Mb.ID,"com.suncity.sunpeople.qa:id/act_imagepreview_download")     # 图片详情【下载】icon
    chat_photo_view = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_image")                        # 聊天窗口中图片、视频（不唯一）
    chat_photo_image_button = (Mb.ID,"com.suncity.sunpeople.qa:id/preview_cb_original")     # 聊天-相册-详情中【原图】按钮
    chat_photo_done_button = (Mb.ID,"com.suncity.sunpeople.qa:id/preview_tv_done")          # 聊天-相册-图片或视频详情中【完成】按钮
    chat_photo_video_view = (Mb.ID,"com.suncity.sunpeople.qa:id/graph_item_iv_img")         # 聊天-相册-选择 （不唯一）
    chat_preview_tv_num = (Mb.ID,"com.suncity.sunpeople.qa:id/preview_tv_num")              # 聊天-相册-图片详情勾选按钮

#--------------【通訊錄】tab页面-----------------------------
    address_book_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_newchat_tv_contacts")      #通訊錄tab
    book_letter_navigation = (Mb.ID,"com.suncity.sunpeople.qa:id/siContactsFilter")         #快速字母导航栏

    book_area = (Mb.ID,"com.suncity.sunpeople.qa:id/tvRegion")                              #地區下拉列表選項
    book_search_input = (Mb.ID,"com.suncity.sunpeople.qa:id/et_search")                     #搜索框
    book_search_count_item = (Mb.ID,"com.suncity.sunpeople.qa:id/tvResultCount")            #搜索結果展示欄
    book_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tvGivenName")                      #下拉列表-用戶暱稱（不唯一））
    book_list_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tvNameTile")                  # 列表-用户名称
    book_user_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/avatar")                         #下拉列表-用戶頭像（不唯一）
    book_user_list = (Mb.ID,"com.suncity.sunpeople.qa:id/llContent")                        #地区下拉列表-用户
    book_indexsidebar = (Mb.ID,"com.suncity.sunpeople.qa:id/siContactsFilter")              #通訊錄列表中-字母導航欄
    book_navigation_letter = (Mb.ID,"com.suncity.sunpeople.qa:id/tvHeadTile")               #通訊錄列表中-首字母（不唯一）
    user_chat_no_login_popup_cancel_button = (Mb.ID,"android:id/button1")                   #聊天界面用户未登陆提示弹框-【取消】按钮
    book_filter_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_filter")                      #筛选icon
    book_filter_page_one = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_area")                    #筛选页-地区选项（不唯一）
    book_filter_done_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")          #筛选页-【完成】按钮
    book_filter_allcleal_button = (Mb.ID,"com.suncity.sunpeople.qa:id/clearBtnView")        #筛选页-【全部清除】按钮
    book_filter_select_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_tick")                 #地区勾选中icon
    book_filter_popup_edit = (Mb.ID,"android:id/button2")                                   #筛选弹框-【编辑筛选】按钮
    book_filter_result = (Mb.ID,"com.suncity.sunpeople.qa:id/tvResultCount")                 #通讯录tab-筛选结果数量展示
    book_allexpend_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tvExpand")                 #「全部展開」按鈕

    book_user_data_email = (Mb.ID,"com.suncity.sunpeople.qa:id/emailView")                       #他人用戶詳情頁郵箱欄
    book_user_data_email_list_option = (Mb.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.TextView\").textContains(\"複製\")")     #点击邮箱下拉选项：复制

    book_personal_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tvMemberInfoGivenName")       #个人资料页面-用户昵称
    book_personal_user_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/avatar")                    #个人资料页面-头像

    book_user_data_section = (Mb.ID,"com.suncity.sunpeople.qa:id/tvDepartmentTitle")            #个人资料页面-隸屬部門
    book_user_data_section_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_department")           #个人资料页面-隸屬部門: 部门名称
    book_user_data_office = (Mb.ID,"com.suncity.sunpeople.qa:id/tvOfficeTitle")                 #个人资料页面-辦公室/場館
    book_user_data_office_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_office")                #个人资料页面-辦公室/場館-办公室名称
    book_user_data_area  = (Mb.ID,"com.suncity.sunpeople.qa:id/tvRegionTitle")                  #个人资料页面-地區*
    book_user_data_area_name = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_region")                  #个人资料页面-地區:地区名称
    book_user_data_colleague = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_departmentalStaff")       #个人资料页面-部門同事
    book_user_data_colleague_itme = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_departmentalStaffCount")         #个人资料页面-部門同事:个数
    colleague_page_title = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_center_title")                #部門同事页面-title
    book_user_data_site_name_label = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_remarks")           #个人资料页面-設定昵稱和標簽
    book_user_data_site_name_label_input = (Mb.ID,"com.suncity.sunpeople.qa:id/act_settingremark_nickName")      #設定昵稱和標簽:輸入框
    book_user_data_site_name_label_page_done = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")     # 設定昵稱和標簽頁面-「完成」按鈕
    colleague_page_more_callout = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_star")                 #个人资料页面-標注信息
    colleague_page_more_rl_file = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_file")                 #个人资料页面-媒體，鏈接和文件
    colleague_page_more_rl_at = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_mention")                #个人资料页面-有提到你的對話

    book_user_data_common_people = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_commonGroup")         #个人资料页面-共同群組
    book_user_data_people_page_titl = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_center_title")     #个人资料页面-共同群众页面title
    book_user_data_people_page_list = (Mb.ID,"com.suncity.sunpeople.qa:id/view_channellist_tv_name")        #个人资料-共同群組 页面群组名称（不唯一）
    book_user_data_sendmessag = (Mb.ID,"com.suncity.sunpeople.qa:id/btn_sendMessage")           #个人资料页面-傳送訊息
    book_user_data_Invite_group = (Mb.ID,"com.suncity.sunpeople.qa:id/btn_inviteChannel")         #个人资料页面-邀请群組
    book_user_data_sendmessag_input = (Mb.ID,"com.suncity.sunpeople.qa:id/msgTextView")           #个人资料页面-跳转聊天界面-输入框
    book_Invite_group_page_list = (Mb.ID,"com.suncity.sunpeople.qa:id/view_channellist_item")       #邀請群組頁面-群組
    personal_page_mute_switch = (Mb.ID,"com.suncity.sunpeople.qa:id/view_loadingswitch_sc")        #靜音、置頂 開關 （不唯一）
    personal_page_find_chat_text = (Mb.ID,"com.suncity.sunpeople.qa:id/cl_findChatContent")         #个人资料页面-查找聊天内容
    personal_page_find_search_input = (Mb.ID,"com.suncity.sunpeople.qa:id/et_search")               #个人资料页面-查找聊天内容:搜索框
    personal_page_find_search_result = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_result_content")      #个人资料页面-查找聊天内容:搜索结果   （不唯一）



#--------------【更多】tab页面-----------------------------
    sunpeople_title = (Mb.ID,"com.suncity.sunpeople.qa:id/iv_center_image")                     #界面顶部-sunpeople
    more_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_newchat_tv_more")                        #更多tab

    more_user_name = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_tv_givename")                 #更多tab-用户昵称
    more_user_jump_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_iv_right")               #更多tab-用户信息跳转icon
    more_user_jump_phone_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_phone_image")            #跳转至用户信息页面-电话icon☎
    chat_window_message_box = (Mb.ID,"com.suncity.sunpeople.qa:id/im_normalitem_text_tv")       #聊天窗口中信息
    chat_window_callout_img = (Mb.ID,"com.suncity.sunpeople.qa:id/msg_toolBar_ivImg")           #聊天窗口中按住信息的標註
    more_callout = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_rl_star")                       #更多tab-【所有標注信息】
    more_rl_file = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_rl_file")                       #更多tab-【所有媒體，鏈接和文件】
    more_rl_at = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_rl_at")                           #更多tab-【有提到你的對話】
    more_callout_page_list = (Mb.CLASS_NAME,"android.widget.RelativeLayout")                    #标注信息页面-标注列表（不唯一）
    more_callout_page_jump_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/recycler_item_select_nextView")  #标注信息页-跳转icon（不唯一）
    more_callout_star = (Mb.ID,"com.suncity.sunpeople.qa:id/starView")                          #聊天窗口-標註☆icon
    more_chat_interface_user_avatar = (Mb.ID,"com.suncity.sunpeople.qa:id/avatarView")           #聊天窗口-用戶頭像
    more_rl_file_media_tab = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_tab_title")                 #【所有媒體，鏈接和文件】- [媒体]tab、[連結]tab、[文件]tab
    more_rl_file_media_tab_list = (Mb.ID,"com.suncity.sunpeople.qa:id/mediaView")                #媒体tab中的选项 （不唯一）
    more_rl_file_tab_list_time = (Mb.ID,"com.suncity.sunpeople.qa:id/headView")                 #媒體、連接、文件tab中時間欄欄
    more_rl_file_link_tab_list = (Mb.ID,"com.suncity.sunpeople.qa:id/titleView")                #连接tab中的选项  （不唯一）
    more_rl_file_file_tab_list = (Mb.ID,"com.suncity.sunpeople.qa:id/titleView")                #文件tab中的选项  （不唯一）
    more_sos_popup = (Mb.ID,"com.suncity.sunpeople.qa:id/dialog_base_tvDone")                   #长按顶部sunpeople-sos确认弹框-【确定】按钮
    moar_at_list_jump_icon = (Mb.ID,"com.suncity.sunpeople.qa:id/recycler_item_select_nextView")        #@列表中跳轉icon （不唯一）
    moar_at_jump_chat_list = (Mb.ID,"com.suncity.sunpeople.qa:id/im_normalitem_text_tv")            #@跳轉聊天窗口-消息欄（不唯一 ）
    more_headphone_mode = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_sc_earphone")                 #更多tab-耳筒模式开关
    more_setup_font_size = (Mb.ID,"com.suncity.sunpeople.qa:id/fra_more_tv_font")              #更多tab-「字體大小」
    more_setup_page_seekbar = (Mb.ID,"com.suncity.sunpeople.qa:id/act_fontsize_seekbar")        #"設置字體大小"頁面底部設置欄
    more_setup_done_button = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_right_title")               #"設置字體大小"頁面-[完成]按鈕
    more_setup_page_copywrting = (Mb.ID,"com.suncity.sunpeople.qa:id/act_fontsize_tv_other")    #"設置字體大小"頁面-文案"選擇下面的形。。。"定位
    chat_es = (Mb.ID, "com.suncity.sunpeople.qa:id/iv_create")                                  # "+"号
    chat_sealed_record = (Mb.ID,"com.suncity.sunpeople.qa:id/tv_create_archived")               #封存记录
    sealed_record_talk_list = (Mb.ID,"com.suncity.sunpeople.qa:id/rl_item_dialog")                        #封存记录对话




