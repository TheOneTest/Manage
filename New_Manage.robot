*** Settings ***
Documentation     新运营管理后台自动化功能测试及数据校验
...               后台地址：http://manage.xiaoyezi.com/#!/login
...               账号：weipeng
...               密码：a123456
Test Teardown     关闭窗口
Default Tags      登录
Library           Selenium2Library
Library           Screenshot
Resource          GUI_keywords.txt
Library           Common/Library/MyLibrary.py

*** Test Cases ***
权限管理--用户管理--创建用户
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 创建用户功能流程，脚本执行完成后，创建一个以“韦鹏”+四位英文字母，为名称的随机角色的用户，邮箱 与 手机号 都为随机数，状态为正常
    [Setup]    登录    weipeng    a123456
    #登录
    wait until element is visible    xpath=//html/body/div/div[1]/nav/ul/li[4]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/nav/ul/li[2]/a/span
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[5]/button
    ${A}    Random_ABC
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[1]/div[1]/input    weipeng_${A}    #输入用户名
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[2]/div[1]/input    韦鹏${A}    #输入真实姓名
    ${B}    Random_NUM
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[3]/div[1]/input    1316208${B}    #输入手机号码
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[4]/div[1]/input    25${A}${B}@qq.com    #输入邮箱
    #Unselect from list by value    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select    1
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select
    ${C}=    evaluate    random.randint(4,9)    random,sys
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select/option[${C}]
    run keyword if    '${C}'=='3'    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[6]/div[1]/input    韦鹏${A}
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[8]/div/button[1]
    wait until page contains    韦鹏    20
    page should contain    韦鹏${A}    创建用户成功
    execute javascript    alert('创建用户韦鹏${A}成功')
    sleep    1
    take screenshot
    [Teardown]    关闭窗口

权限管理--用户管理--用户编辑
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 编辑用户功能流程，脚本执行完成后，随机对列表中的一个用户进行编辑操作，主要操作为 修改姓名、手机号、邮箱
    [Setup]    登录    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/nav/ul/li[2]/a/span
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[1]    20
    click element    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[1]
    ${A}    Random_ABC
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[2]/div[1]/input    20
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[2]/div[1]/input    张鹏${A}    #输入真实姓名
    ${B}    Random_NUM
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[3]/div[1]/input    1316208${B}    #输入手机号码
    input text    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[4]/div[1]/input    88${A}${B}@qq.com    #输入邮箱
    #Unselect from list by value    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select    1
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select
    ${C}=    evaluate    random.randint(1,8)    random,sys
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select/option[${C}]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[5]/div[1]/select/option[${C}]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div/form/div[8]/div/button[1]
    wait until page contains    韦鹏
    page should contain    张鹏${A}
    page should contain    1316208${B}
    page should contain    88${A}${B}@qq.com
    [Teardown]

权限管理--用户管理--冻结解冻
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 冻结与解冻用户功能流程，脚本主要执行用户冻结与解冻操作
    [Setup]
    [Template]
    [Timeout]
    wait until element is visible    xpath=//html/body/div/div[1]/nav/ul/li[4]/a/span
    ${static_star}=    get text    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]
    click element    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[3]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[4]/div/div/div[3]/button[1]
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[3]    20
    ${static_end}=    get text    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]
    run keyword if    '${static_star}'=='${static_end}'    click element    ${static_star} 设置为 ${static_end} 失败
    ...    ELSE    log    ${static_star} 设置为 ${static_end} 成功
    click element    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[3]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[4]/div/div/div[3]/button[1]
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[3]    20
    ${static}=    get text    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]
    run keyword if    '${static_star}'=='${static_end}'    click element    ${static_end} 设置为 ${static} 失败
    ...    ELSE    log    ${static_end} 设置为 ${static} 成功
    [Teardown]

权限管理--用户管理--用户查询
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 用户搜索功能流程，脚本主要执行：
    ...    用户名搜索，手机号搜索，模糊搜索，联合搜索，及角色搜索
    [Setup]
    ${rom_num}=    evaluate    random.randint(2,49)    random,sys
    ${rom_list}=    evaluate    random.randint(2,8)    random,sys
    ${get_name}=    get text    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[${rom_num}]/td[2]
    ${get_name_y}=    get text    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[${rom_num}-1]/td[2]
    #click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[3]/input    #点击查询
    input text    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[1]/input    ${get_name}
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[4]/input    #点击查询
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/table/thead/tr/th[1]    20
    page should contain    ${get_name}    搜索结果正确
    page should not contain    ${get_name_y}    页面中不存在${get_name_y}
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[4]/button    #清除搜索条件
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[2]/select    #选择管理员
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[2]/select/option[${rom_list}]    #选择管理员
    ${num_c}    get matching xpath count    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr
    ${name_list}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[2]/select/option[${rom_list}]
    set selenium speed    0
    : FOR    ${i}    IN RANGE    ${num_c}
    \    ${r}=    get text    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[4]/td[5]
    \    run keyword if    '${r}'=='${name_list}'    log    搜索结果正确
    \    ...    ELSE    click element    搜索结果不正确
    set selenium speed    0.5
    [Teardown]

权限管理--用户管理--重置密码
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 用户重置密码功能流程，脚本主要执行用户重置密码操作
    [Setup]
    click element    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[4]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[4]/div/div/div[3]/button[1]
    log    重置密码成功
    #page should contain element    xpath=//html/body/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/button[5]
    [Teardown]    关闭窗口

权限管理--角色管理--角色筛选
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 角色管理页面用户功能流程，脚本主要执行角色的查询筛选功能
    ...    包括：角色状态查询、角色名查询、联合查询
    [Setup]    登录    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/nav/ul/li[1]/a/span
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/select    5
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/select
    ${C}=    evaluate    random.randint(1,10)    random,sys
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/select/option[${C}]
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]    5
    [Teardown]    关闭窗口

权限管理--角色管理--新建/设置/修改/删除
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面， 角色管理页面用户功能流程，脚本主要执行角色的新建、设置、修改、删除 操作
    [Setup]    登录    weipeng    a123456
    [Timeout]
    权限管理--创建角色
    权限管理--修改角色
    权限管理--删除角色
    [Teardown]    关闭窗口

权限管理--菜单管理--菜单操作
    [Documentation]    （PRE 环境）运营管理后台，权限管理 页面，菜单管理页面用户功能流程，脚本主要执行菜单的新建，编辑删除功能
    [Setup]    登录    weipeng    a123456
    #新建一级菜单
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[4]/nav/ul/li[3]/a/span
    ${a}=    run keyword and return status    检测内容是否存在    测试一级菜单
    ${b}=    run keyword and return status    检测内容是否存在    测试二级菜单
    run keyword if    ${a}==False    log    二级菜单不存在
    ...    ELSE IF    ${b}==True    删除二级菜单
    ...    ELSE    删除一级菜单
    权限管理--新建菜单
    删除二级菜单
    [Teardown]    关闭窗口

白名单管理--添加白名单列表(机构)
    [Documentation]    （PRE 环境）运营管理后台，白名单管理页面功能流程，脚本主要执行机构添加白名单，及添加后机构列表信息屏蔽功能
    [Setup]    登录    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[1]/a/span
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]
    ${a}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]
    ${b}=    substring num    ${a}    #获取机构代码编号
    log    ${b}
    click element    xpath=//html/body/div/div[1]/nav/ul/li[5]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[5]/nav/ul/li/a/span
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/button
    click element    xpath=//.//*[@id='school']
    input text    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[2]/div/input    ${b}
    click button    xpath=//html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/button[1]
    page should contain    ${b}    白名单列表是否添加成功    #检查白名单列表是否添加成功
    #检查教室分析页面是否移除成功
    sleep    2
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[1]/a/span
    go to    http://manage-pre.xiaoyezi.com/#!/stat/school
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]
    page should not contain    ${b}    白名单已生效
    白名单管理--移除白名单（机构）
    [Teardown]    关闭窗口

白名单管理--添加白名单列表(代理商)
    [Documentation]    （PRE 环境）运营管理后台，白名单管理页面功能流程，脚本主要执行代理商添加白名单，及添加后代理商列表信息屏蔽功能
    [Setup]    登录    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/a
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[3]/a/span
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]    5
    ${a}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]
    click element    xpath=//html/body/div/div[1]/nav/ul/li[5]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[5]/nav/ul/li/a/span
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/button
    input text    xpath=//html/body/div/div[2]/div/div[2]/div[1]/form/div[2]/div/input    ${a}
    click button    xpath=//html/body/div/div[2]/div/div[2]/div[1]/div[4]/div/button[1]
    page should contain    ${a}    白名单列表添加成功    #检查白名单列表是否添加成功
    #检查教室分析页面是否移除成功
    sleep    1
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[3]/a/span
    go to    http://manage-pre.xiaoyezi.com/#!/stat/agentInfo
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]    5
    page should not contain    ${a}    白名单已生效
    白名单管理--移除白名单（代理商）
    [Teardown]    关闭窗口

机构督导--机构位置信息--查看详情
    [Documentation]    （线上环境）运营管理后台机构督导 -- 机构位置信息 页面 数据校验，详情页面数据校验
    ...    包括：机构名称、机构代码、机构地址、教室实际地址等信息校验
    [Setup]    登录pro    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[3]/a
    click element    xpath=//html/body/div/div[1]/nav/ul/li[3]/nav/ul/li[1]/a/span
    ${a_list}=    evaluate    random.randint(50,100)    random,sys
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]    5
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/select
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[2]/div[2]/div/select/option[5]
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[${a_list}]/td[1]    5
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[${a_list}]/td[1]
    ${list_name}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[${a_list}]/td[1]
    ${list_add}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[${a_list}]/td[2]
    ${lreal_add}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[${a_list}]/td[3]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[2]/table/tbody/tr[${a_list}]/td[6]/button
    #page should contain    ${list_name}    详情页机构名称显示正常
    ${new_add}=    substr    ${list_add}
    page should contain    ${new_add}    详情页资料地址显示正常
    page should contain    ${lreal_add}    详情页实际显示正常
    [Teardown]    关闭窗口

机构督导--机构续费巡查
    [Documentation]    （线上环境）运营管理后台机构督导 -- 机构续费巡查 页面 数据校验，详情页面数据校验
    [Setup]    登录pro    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[3]/a
    click element    xpath=//html/body/div/div[1]/nav/ul/li[3]/nav/ul/li[2]/a/span
    ${a_list}=    evaluate    random.randint(50,100)    random,sys
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]    5
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/select
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/select/option[5]
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[${a_list}]/td[1]    5
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[${a_list}]/td[1]
    ${list_name}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[${a_list}]/td[1]
    ${list_uname}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[${a_list}]/td[6]
    click element    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[${a_list}]/td[11]/button
    ${list_get}    get text    xpath=//html/body/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div[1]/h4
    page should contain    ${list_name}-${list_uname}    5    #验证详情页机构名称是否正确
    [Teardown]    关闭窗口

设置--修改密码
    [Documentation]    （线上环境）运营管理后台，修改用户登录密码功能流程，脚本主要执行账号的密码修改及新密码登录功能
    [Setup]    登录pro    weipeng    a123456
    设置--修改密码    a123456    b123456
    关闭窗口
    ${edit_password}=    run keyword and return status    登录pro    weipeng    b123456
    run keyword if    '${edit_password}'=='True'    设置--修改密码    b123456    a123456
    ...    ELSE    execute javascript    alert('修改密码失败')
    [Teardown]    关闭窗口

统计信息 -- 代理商信息
    [Documentation]    （线上环境）运营管理后台 \ 统计信息 -- 代理商信息 页面 功能自动化测试
    ...    主要校验：
    ...    代理商信息页面 \ 数据是否显示正常
    ...    机构信息页面数据是否显示正常、详情页面信息显示校验
    ...    机构位置页面数据是否显示正常、详情页面信息显示校验
    ...    机构续费巡查页面数据是否显示正常、详情页面信息显示校验
    [Setup]    登录pro    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/a/span
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[3]/a/span
    wait until element is visible    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]    15
    ${list_num}=    get matching xpath count    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr
    ${list_index}=    evaluate    random.randint(1,${list_num})    random,sys
    ${location}=    get text    xpath=//html/body/div/div[2]/div/div[2]/div[3]/table/tbody/tr[${list_index}]/td[6]
    机构信息页面检测    ${list_index}    ${location}
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[3]/a/span
    机构位置页面检测    ${list_index}
    click element    xpath=//html/body/div/div[1]/nav/ul/li[2]/nav/ul/li[3]/a/span
    sleep    1
    机构续费巡查页面检测    ${list_index}
    [Teardown]    关闭窗口

总览--尤克里里教室
    [Documentation]    （线上环境）运营管理后台校验尤克里里教室数据是否显示正常
    ...    校验内容包括：机构总数、教室总数
    [Setup]    登录pro    weipeng    a123456
    click element    xpath=//html/body/div/div[1]/nav/ul/li[1]/nav/ul/li[3]/a/span    #打开尤克里里教室页面
    ${macro}=    get text    xpath=//html/body/div/div[2]/div/div/div/ul/li[1]/span[2]
    ${class}=    get text    xpath=//html/body/div/div[2]/div/div/div/ul/li[2]/span[2]
    inspect_ykll    ${macro}    ${class}
    [Teardown]    关闭窗口

*** Keywords ***
