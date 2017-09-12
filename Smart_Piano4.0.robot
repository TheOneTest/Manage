*** Settings ***
Suite Setup
Suite Teardown
Library           AppiumLibrary
Library           Screenshot
Library           Common/Library/MyAppLibrary.py
Resource          sp4.0_keywords.txt
Library           Common/Library/Exceledit.py

*** Test Cases ***
智能钢琴--曲谱视频资源监测
    [Setup]    启动程序
    wait until element is visible    name=曲集
    click element    name=曲集
    sleep    3
    #click a point    415    500
    #监测课程章节
    遍历所有曲谱
    [Teardown]    关闭程序

智能钢琴--游戏资源监测
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.HorizontalScrollView[@resource-id=\"com.theonepiano.smartpiano:id/tab\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView[1]
    click element    xpath=//android.widget.HorizontalScrollView[@resource-id=\"com.theonepiano.smartpiano:id/tab\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView[1]
    遍历所有游戏
    [Teardown]    关闭程序

(手机)智能钢琴--个人中心--导航检测
    [Setup]    启动程序
    wait until element is visible    name=我的
    #click element    name=我的
    #click element    xpath=//android.widget.TextView[@resource-id=\"com.theonepiano.smartpiano:id/tv_pref_name\"]
    #sleep    10
    ${count}=    get matching xpath count    xpath=//android.widget.ImageView[@resource-id=\"com.theonepiano.smartpiano:id/iv_collection_cover\"]
    click element    xpath=//android.widget.ImageView[@resource-id=\"com.theonepiano.smartpiano:id/iv_collection_cover\"][3]
    sleep    10
    [Teardown]    关闭程序

(手机)只能钢琴--个人中心--我的收藏
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    wait until element is visible    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    name=我的
    wait until element is visible    id=com.theonepiano.smartpiano:id/title
    ${username}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]
    run keyword if    '${username}'=='登录后收藏琴谱,手机平板多端同步'    我的页面登录账号
    wait until element is visible    name=我的收藏    15
    click element    name=我的收藏
    #查询我的收藏数据量
    清空我的收藏
    [Teardown]    关闭程序

智能钢琴--用户注册
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    检查用户登录状态
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/regist    #点击注册按钮
    ${em_name}=    random abc
    input text    id=com.theonepiano.smartpiano:id/email    wp${em_name}
    sleep    0.3
    input text    id=com.theonepiano.smartpiano:id/password    a123456
    click element    id=com.theonepiano.smartpiano:id/email
    sleep    1
    输入邮箱文本
    click element    id=com.theonepiano.smartpiano:id/action_register
    #校验是否注册成功
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    ${real_em}=    get text    id=com.theonepiano.smartpiano:id/avatar_title
    run keyword if    'wp${em_name}@qq.com'=='${real_em}'    log    用户注册成功
    ...    ELSE    click element    用户注册失败
    Write_Excel    wp${em_name}@qq.com
    log    wp${em_name}@qq.com
    log    ${real_em}
    导航退出登录
    Capture Page Screenshot
    [Teardown]    关闭程序

智能钢琴--用户登录
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    检查用户登录状态
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    用户登录    wp123@qq.com    a123456
    导航退出登录
    [Teardown]    关闭程序

智能钢琴--修改密码
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    检查用户登录状态
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    sleep    0.3
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    sleep    0.3
    input text    id=com.theonepiano.smartpiano:id/email    wp123
    sleep    0.3
    input text    id=com.theonepiano.smartpiano:id/password    a123456
    click element    id=com.theonepiano.smartpiano:id/email
    sleep    1
    输入邮箱文本
    press keycode    4
    click element    id=com.theonepiano.smartpiano:id/action_login
    sleep    0.5
    wait until element is visible    id=com.theonepiano.smartpiano:id/drawer_icon
    #修改密码
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    click element    name=更改密码
    修改密码    a123456    b123456
    退出登录状态
    #使用新密码登录
    click element    id=com.theonepiano.smartpiano:id/login    #点击进入登录页面
    sleep    0.3
    input text    id=com.theonepiano.smartpiano:id/email    wp123
    sleep    0.3
    input text    id=com.theonepiano.smartpiano:id/password    b123456
    click element    id=com.theonepiano.smartpiano:id/email
    sleep    1
    输入邮箱文本
    press keycode    4
    sleep    1
    click element    id=com.theonepiano.smartpiano:id/action_login
    click element    id=com.theonepiano.smartpiano:id/change_password
    修改密码    b123456    a123456
    退出登录状态
    [Teardown]    关闭程序

智能钢琴--曲谱搜索
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/search
    wait until element is visible    id=com.theonepiano.smartpiano:id/search_content_view    15
    input text    id=com.theonepiano.smartpiano:id/search_content_view    canon
    press keycode    66
    wait until element is visible    xpath=//android.widget.ListView[@resource-id=\"com.theonepiano.smartpiano:id/list_view\"]/android.widget.LinearLayout[2]
    ${list_num}=    get matching xpath count    xpath=//android.widget.ListView[@resource-id=\"com.theonepiano.smartpiano:id/list_view\"]/android.widget.LinearLayout
    run keyword if    ${list_num}>=1    page should contain text    卡农    10
    ...    ELSE    click element    曲谱搜索存在问题，列表为空    #验证搜索结果中是否存在卡农
    ${index}=    random num
    ${qupu}=    get text    xpath=//android.widget.RadioButton[@resource-id=\"com.theonepiano.smartpiano:id/tab_song\"]
    曲谱搜索--随机进入曲谱主页    ${index}
    log    ${qupu}
    click element    id=com.theonepiano.smartpiano:id/tab_lesson    #点击视频分页
    ${vedio}=    get text    id=com.theonepiano.smartpiano:id/tab_lesson
    log    ${vedio}
    ${kala}=    get text    id=com.theonepiano.smartpiano:id/tab_kara
    log    ${kala}
    sleep    1
    click element    id=com.theonepiano.smartpiano:id/tab_song
    [Teardown]    关闭程序

智能钢琴--名曲速成--列表数据校验
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_music_lab\"]/android.widget.ImageView[1]
    sleep    3
    ${list_count}=    get matching xpath count    xpath=//android.widget.GridView[@resource-id=\"com.theonepiano.smartpiano:id/song_grid\"]/android.widget.RelativeLayout
    log    ${list_count}
    run keyword if    ${list_count}<1    click element    名曲速成列表中无数据显示
    ...    ELSE    log    列表中存在数据
    ${name1}=    名曲速成--列表数据验证
    ${name2}=    名曲速成--列表数据验证
    ${name3}=    名曲速成--列表数据验证
    ${name4}=    名曲速成--列表数据验证
    ${name5}=    名曲速成--列表数据验证
    @{name}    create list    ${name1}    ${name2}    ${name3}    ${name4}    ${name5}
    list_Loading    ${name}
    [Teardown]    关闭程序

智能钢琴--名曲速成--曲谱详情页
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_music_lab\"]/android.widget.ImageView[1]
    ${num}    evaluate    random.randint(1,9)    random
    随机向上滑动    ${num}
    wait until element is visible    xpath=//android.widget.GridView[@resource-id=\"com.theonepiano.smartpiano:id/song_grid\"]/android.widget.RelativeLayout[1]
    click element    xpath=//android.widget.GridView[@resource-id=\"com.theonepiano.smartpiano:id/song_grid\"]/android.widget.RelativeLayout[1]
    曲谱详情页数据校验
    曲谱详情页试听功能检测
    sleep    1
    click element    id=com.theonepiano.smartpiano:id/start_btn
    sleep    1
    wait until element is visible    xpath=//android.view.View    60
    sleep    10
    press keycode    4    #返回上个页面
    sleep    2
    click element    name=进阶
    sleep    0.5
    曲谱详情页数据校验
    [Teardown]    关闭程序

智能钢琴--视频教程--儿童教程
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_video\"]/android.widget.ImageView[1]
    儿童视频教程页面数据监测
    儿童视频教程详情页校验
    随机播放儿童视频教程
    [Teardown]    关闭程序

智能钢琴--视频教程--成人教程
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_video\"]/android.widget.ImageView[1]
    wait until element is visible    name=成人教程
    click element    name=成人教程
    ${num}    evaluate    random.randint(1,5)    random
    随机向上滑动    ${num}
    视频教程页面数据监测
    视频教程详情页校验
    #随机播放视频教程
    [Teardown]    关闭程序

智能钢琴--卡拉游戏--娱乐
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    ${name1}=    卡拉游戏--娱乐列表数据验证
    ${name2}=    卡拉游戏--娱乐列表数据验证
    ${name3}=    卡拉游戏--娱乐列表数据验证
    ${name4}=    卡拉游戏--娱乐列表数据验证
    ${name5}=    卡拉游戏--娱乐列表数据验证
    @{name}    create list    ${name1}    ${name2}    ${name3}    ${name4}    ${name5}
    list_Loading    ${name}
    进入卡拉游戏详情页
    [Teardown]    关闭程序

智能钢琴--卡拉游戏--学习
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    [Teardown]    关闭程序

智能钢琴--卡拉游戏--弹唱
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    [Teardown]    关闭程序

智能钢琴--卡拉游戏--亲子
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    [Teardown]    关闭程序

智能钢琴--弹奏历史

(平板）智能钢琴--卡拉游戏--娱乐
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    ${name1}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name2}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name3}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name4}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name5}=    (平板)卡拉游戏--娱乐列表数据验证
    @{name}    create list    ${name1}    ${name2}    ${name3}    ${name4}    ${name5}
    list_Loading    ${name}
    进入卡拉游戏详情页
    [Teardown]    关闭程序

(平板）智能钢琴--卡拉游戏--学习
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    click element    name=学习
    ${name1}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name2}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name3}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name4}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name5}=    (平板)卡拉游戏--娱乐列表数据验证
    @{name}    create list    ${name1}    ${name2}    ${name3}    ${name4}    ${name5}
    list_Loading    ${name}
    进入卡拉游戏详情页
    [Teardown]    关闭程序

(平板）智能钢琴--卡拉游戏--弹唱
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    click element    name=弹唱
    ${name1}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name2}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name3}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name4}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name5}=    (平板)卡拉游戏--娱乐列表数据验证
    @{name}    create list    ${name1}    ${name2}    ${name3}    ${name4}    ${name5}
    list_Loading    ${name}
    进入卡拉游戏详情页
    [Teardown]    关闭程序

(平板）智能钢琴--卡拉游戏--亲子
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    click element    name=亲子
    ${name1}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name2}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name3}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name4}=    (平板)卡拉游戏--娱乐列表数据验证
    ${name5}=    (平板)卡拉游戏--娱乐列表数据验证
    @{name}    create list    ${name1}    ${name2}    ${name3}    ${name4}    ${name5}
    list_Loading    ${name}
    进入卡拉游戏详情页
    [Teardown]    关闭程序

(平板）智能钢琴--卡拉游戏--弹奏历史
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    wait until element is visible    id=com.theonepiano.smartpiano:id/history
    click element    id=com.theonepiano.smartpiano:id/history    #点击弹奏历史按钮
    Capture Page Screenshot
    [Teardown]    关闭程序

(平板）智能钢琴--个人中心--导航检测
    [Setup]    启动程序
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_kara\"]/android.widget.ImageView[1]
    wait until element is visible    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    name=我的
    ${list1}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]
    ${list2}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]
    ${list3}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.TextView[1]
    ${list4}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.TextView[1]
    ${list5}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.TextView[1]
    ${list6}=    get text    xpath=//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.TextView[1]
    inspect_usercenter    ${list1}    ${list2}    ${list3}    ${list4}    ${list5}    ${list6}
    [Teardown]    关闭程序
