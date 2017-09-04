*** Settings ***
Suite Setup       启动程序
Suite Teardown    关闭程序
Library           AppiumLibrary
Library           Screenshot
Library           Common/Library/MyAppLibrary.py
Resource          func_keywords.txt

*** Test Cases ***
智能钢琴--曲谱搜索
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
    [Teardown]    返回主界面

智能钢琴--用户注册
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    检查用户登录状态
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    click element    id=com.theonepiano.smartpiano:id/regist    #点击注册按钮
    ${em_name}=    random abc
    input text    id=com.theonepiano.smartpiano:id/email    wp${em_name}
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
    log    wp${em_name}@qq.com
    log    ${real_em}
    导航退出登录
    Capture Page Screenshot

智能钢琴--用户登录
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    检查用户登录状态
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    input text    id=com.theonepiano.smartpiano:id/email    wp123
    input text    id=com.theonepiano.smartpiano:id/password    a123456
    click element    id=com.theonepiano.smartpiano:id/email
    sleep    1
    输入邮箱文本
    press keycode    4
    click element    id=com.theonepiano.smartpiano:id/action_login
    wait until element is visible    id=com.theonepiano.smartpiano:id/drawer_icon
    #校验是否登录成功
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    ${real_em}=    get text    id=com.theonepiano.smartpiano:id/avatar_title
    run keyword if    'wp123@qq.com'=='${real_em}'    log    用户登录成功
    ...    ELSE    click element    用户登录失败
    log    ${real_em}

智能钢琴--修改密码
    wait until element is visible    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]    15
    click element    xpath=//android.widget.FrameLayout[@resource-id=\"com.theonepiano.smartpiano:id/btn_led\"]/android.widget.ImageView[1]
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    检查用户登录状态
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    input text    id=com.theonepiano.smartpiano:id/email    wp123
    input text    id=com.theonepiano.smartpiano:id/password    a123456
    click element    id=com.theonepiano.smartpiano:id/email
    sleep    1
    输入邮箱文本
    press keycode    4
    click element    id=com.theonepiano.smartpiano:id/action_login
    wait until element is visible    id=com.theonepiano.smartpiano:id/drawer_icon
    #修改密码
    click element    id=com.theonepiano.smartpiano:id/drawer_icon
    click element    id=com.theonepiano.smartpiano:id/account_view    #点击进入登录页面
    click element    name=更改密码
    修改密码
